import os
import subprocess
import shutil
import re
import markdown
from bs4 import BeautifulSoup
from atlassian import Confluence

#playwright need to be installed

# Enhanced documentation prompt
DOC_PROMPT = """
You are an AI Documentation Agent. Your task is to create developer-friendly and non-technical-friendly documentation for the #file:cloned_repo project repository.

1. ./docs/index.md -> Overview, tools used, overall explanation of how this project is laid up, and links to all docs
2. ./docs/architecture.md -> System architecture, flow diagrams
3. ./docs/database.md -> Supported DBs, ERD, table descriptions
4. ./docs/classes.md -> Classes, UML diagram, plain English explanation
5. ./docs/web.md -> REST API endpoints, pages, navigation flow
6. Ensure readability for both devs and non-tech users

Thes Docs are already created with placeholders. Your job is to fill in the content based on the codebase analysis.

Instead of giving one-liner descriptions, provide detailed explanations with examples where applicable.
"""


def clone_repo(repo_url, dest_folder="cloned_repo"):
    # Try to remove existing directory
    if os.path.exists(dest_folder):
        try:
            # First, try to remove read-only flags recursively on Windows
            if os.name == "nt":  # Windows systems
                subprocess.run(
                    ["attrib", "-R", dest_folder + "\\*.*", "/S"], check=False
                )
            shutil.rmtree(dest_folder)
        except Exception as e:
            print(f"⚠️ Warning: Could not completely remove old directory: {e}")
            # If removal failed, try with a new name
            base_name = dest_folder
            counter = 1
            while os.path.exists(dest_folder):
                dest_folder = f"{base_name}_{counter}"
                counter += 1
            print(f"👉 Using alternative folder: {dest_folder}")

    try:
        subprocess.run(["git", "clone", repo_url, dest_folder], check=True)
        print(f"✅ Repository cloned into: {dest_folder}")
        return dest_folder
    except subprocess.CalledProcessError as e:
        print("❌ Error cloning repository:", e)
        return None

def replace_mermaid_with_png(content, output_dir, file_prefix):
    """
    Convert all mermaid blocks in content to PNGs.
    Returns updated content and list of generated PNG paths.
    """
    matches = re.findall(r"```mermaid\n(.*?)```", content, re.DOTALL)
    generated_pngs = []

    for i, code in enumerate(matches, start=1):
        png_file = os.path.join(output_dir, f"{file_prefix}_diagram_{i}.png")
        mmd_file = os.path.join(output_dir, f"{file_prefix}_diagram_{i}.mmd")

        # Write temp .mmd
        with open(mmd_file, "w", encoding="utf-8") as f:
            f.write(code.strip())

        # Generate PNG
        subprocess.run(["mmdc", "-i", mmd_file, "-o", png_file], check=True)
        generated_pngs.append(png_file)

        # Replace mermaid block with Confluence image macro
        ac_image = f"""<ac:image><ri:attachment ri:filename="{os.path.basename(png_file)}" /></ac:image>"""
        content = content.replace(f"```mermaid\n{code}```", ac_image)

        if os.path.exists(mmd_file):
            os.remove(mmd_file)

    return content, generated_pngs


def md_to_confluence_storage(md_content: str) -> str:
    """
    Convert Markdown content into Confluence storage format XHTML.
    Mermaid/PlantUML blocks are already replaced as PNG by replace_mermaid_with_png,
    so we only handle code, tables, etc.
    """
    html_content = markdown.markdown(
        md_content,
        extensions=["fenced_code", "tables"]
    )
    soup = BeautifulSoup(html_content, "html.parser")

    # Handle fenced code blocks
    for pre in soup.find_all("pre"):
        code = pre.code
        if code and code.has_attr("class"):
            lang_classes = code["class"]

            # Skip mermaid/plantuml (handled earlier)
            if "language-mermaid" in lang_classes or "language-plantuml" in lang_classes:
                continue

            # Other code blocks → wrap in Confluence <ac:structured-macro>
            code_block = soup.new_tag("ac:structured-macro", **{"ac:name": "code"})
            param = soup.new_tag("ac:parameter", **{"ac:name": "language"})
            param.string = lang_classes[0].replace("language-", "")
            code_macro_body = soup.new_tag("ac:plain-text-body")
            code_macro_body.string = code.get_text()
            code_block.append(param)
            code_block.append(code_macro_body)
            pre.replace_with(code_block)

    return str(soup)

def convert_links(content, parent_page_title, child_pages):
    """
    Convert markdown links like [Architecture](architecture.md)
    to Confluence links like [Architecture|Parent Page Title^Architecture]
    """
    def replacer(match):
        text = match.group(1)
        link = match.group(2)
        if link.endswith(".md"):
            child_title = link.replace(".md", "").capitalize()
            if child_title in child_pages:
                return f"[{text}|{parent_page_title}^{child_title}]"
        return match.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replacer, content)

def publish_to_confluence(confluence_url, space_key, docs_folder, username, api_token):
    confluence = Confluence(
        url=confluence_url,
        username=username,
        password=api_token
    )

    parent_page_id = None

    # Ensure index.md is processed first
    md_files = sorted([f for f in os.listdir(docs_folder) if f.endswith(".md")])
    if "index.md" in md_files:
        md_files.remove("index.md")
        md_files = ["index.md"] + md_files

    for filename in md_files:
        file_path = os.path.join(docs_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        file_prefix = os.path.splitext(filename)[0]

        # Convert mermaid -> PNG + replace with <ac:image>
        content, generated_pngs = replace_mermaid_with_png(content, os.path.dirname(file_path), file_prefix)

        # Convert Markdown -> Confluence storage
        page_body = md_to_confluence_storage(content)

        if filename == "index.md":
            page_title = content.splitlines()[0].lstrip("# ").strip() or "Project Documentation"
            parent_page = confluence.create_page(
                space=space_key,
                title=page_title,
                body=page_body,
                type="page",
                representation="storage"
            )
            parent_page_id = parent_page["id"]
            target_page_id = parent_page_id
            print(f"📤 Published parent page: {page_title} (ID: {parent_page_id})")
        else:
            page_title = filename.replace(".md", "").capitalize()
            if parent_page_id:
                child_page = confluence.create_page(
                    space=space_key,
                    title=page_title,
                    body=page_body,
                    parent_id=parent_page_id,
                    type="page",
                    representation="storage"
                )
                target_page_id = child_page["id"]
                print(f"📤 Published child page: {page_title} (ID: {target_page_id})")
            else:
                print(f"⚠️ Skipped {page_title}, parent page not created yet!")
                continue

        # Attach all PNGs
        for png in generated_pngs:
            confluence.attach_file(png, page_id=target_page_id)
            print(f"🖼️ Attached diagram: {os.path.basename(png)}")

# def publish_to_confluence(confluence_url, space_key, docs_folder, username, api_token):
#     confluence = Confluence(
#         url=confluence_url,
#         username=username,
#         password=api_token
#     )

#     parent_id = None
#     child_pages = {}

#     # Step 1: Always handle index.md first
#     index_file = os.path.join(docs_folder, "index.md")
#     if os.path.exists(index_file):
#         with open(index_file, "r", encoding="utf-8") as f:
#             content = f.read()

#         # Extract project title from first heading
#         first_line = content.splitlines()[0].strip()
#         if first_line.startswith("#"):
#             page_title = first_line.lstrip("#").strip()
#         else:
#             page_title = "Project Documentation"

#         parent_page_title = page_title

#         # Convert links in index.md before publishing
#         content = convert_links(content, parent_page_title, child_pages)

#         parent_page = confluence.create_page(
#             space=space_key,
#             title=page_title,
#             body=content,
#             parent_id=None,
#             type="page",
#             representation="storage"
#         )
#         parent_id = parent_page["id"]
#         print(f"📤 Published parent page: {page_title} (ID: {parent_id})")
#     else:
#         print("⚠️ index.md not found, cannot create parent page!")
#         return

#     # Step 2: Publish all other docs as children
#     for filename in os.listdir(docs_folder):
#         if not filename.endswith(".md") or filename == "index.md":
#             continue

#         filepath = os.path.join(docs_folder, filename)
#         with open(filepath, "r", encoding="utf-8") as f:
#             content = f.read()

#         # Use first heading if present, else filename
#         first_line = content.splitlines()[0].strip()
#         if first_line.startswith("#"):
#             title = first_line.lstrip("#").strip()
#         else:
#             title = filename.replace(".md", "").capitalize()

#         try:
#             confluence.create_page(
#                 space=space_key,
#                 title=title,
#                 body=content,
#                 parent_id=parent_id,
#                 type="page",
#                 representation="storage"
#             )
#             child_pages[title] = True
#             print(f"📄 Published child page: {title}")
#         except Exception as e:
#             print(f"❌ Failed to publish {title}: {e}")

def show_prompt():
    print("\n📄 Documentation Generation Prompt:")
    print("=" * 60)
    print(DOC_PROMPT)
    print("=" * 60)


def generate_docs(repo_path):
    """Generate documentation structure with meaningful placeholders."""
    # Create docs folder parallel to the repository
    docs_folder = os.path.join(os.path.dirname(repo_path), "docs")
    os.makedirs(docs_folder, exist_ok=True)

    # Documentation templates
    templates = {
        "index.md": """# Project Overview

## Purpose
Brief description of the project's purpose and goals.

## Audience
- Developers
- Non-technical users

## Documentation Sections
- [Architecture](architecture.md)
- [Database](database.md)
- [Classes](classes.md)
- [Web](web.md)
""",
        "architecture.md": """# System Architecture

## Overview
High-level system architecture description.

## Components
- Frontend
- Backend
- Database

## Flow Diagrams
```
[Component Diagram Placeholder]
```
""",
        "database.md": """# Database Design

## Supported Databases
List of supported databases

## Entity-Relationship Diagram
```
[ERD Diagram Placeholder]
```

## Tables
- Table 1
- Table 2
""",
        "classes.md": """# Classes and Components

## Overview
Main classes and components overview

## UML Diagram
```
[UML Diagram Placeholder]
```

## Plain English Descriptions
- Component 1: Description
- Component 2: Description
""",
        "web.md": """# Web Documentation

## API Endpoints
- GET /endpoint1
- POST /endpoint2

## Pages
- Page 1
- Page 2

## Navigation Flow
1. Step 1
2. Step 2
""",
    }

    # Create documentation files with templates
    for filename, template in templates.items():
        file_path = os.path.join(docs_folder, filename)
        with open(file_path, "w", encoding="utf-8") as doc_file:
            doc_file.write(template)
        print(f"✅ Created {filename}")

    print("\n📚 Documentation structure created at:", docs_folder)
    print("💡 Next: Use an LLM to fill in the content based on repository analysis")


if __name__ == "__main__":
    repo_url = input("🔗 Enter GitHub repository URL: ").strip()
    repo_path = clone_repo(repo_url)

    if repo_path:
        #generate_docs(repo_path)
        show_prompt()
        input("\n⚡ Press Enter after feeding this prompt to your LLM...")
        # Delete the cloned_repo folder after documentation is created
        try:
            if os.path.exists(repo_path):
                shutil.rmtree(repo_path, ignore_errors=True)
                print(f"🗑️ Deleted cloned repository folder: {repo_path}")
        except Exception as e:
            print(f"⚠️ Warning: Could not delete cloned repository folder: {e}")
        print("\n🎉 Documentation generation completed successfully!")

        confluence_url = "https://barathsundar03.atlassian.net/wiki"
        space_key = "~712020b66a49d1b1b44a6d9b897ba1631b9b7f"
        username = "barathsundar03@gmail.com"
        api_token=

        docs_folder = os.path.join(os.path.dirname(repo_path), "docs")
        publish_to_confluence(confluence_url, space_key, docs_folder, username, api_token)
