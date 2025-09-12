import os
import subprocess
import shutil

# Enhanced documentation prompt
DOC_PROMPT = """
You are an AI Documentation Agent. Your task is to create developer-friendly and non-technical-friendly documentation for the #file:cloned_repo project repository.

1. ./docs/index.md -> Overview, tools used, overall explanation of how this project is laid up, and links to all docs
2. ./docs/architecture.md -> System architecture, flow diagrams
3. ./docs/database.md -> Supported DBs, ERD, table descriptions
4. ./docs/classes.md -> Classes, UML diagram, plain English explanation
5. ./docs/web.md -> REST API endpoints, pages, navigation flow
6. Ensure readability for both devs and non-tech users
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
            shutil.rmtree(dest_folder, ignore_errors=True)
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
        generate_docs(repo_path)
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
