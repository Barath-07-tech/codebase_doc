# The Wild Oasis - Project Overview

## Purpose
The Wild Oasis is a comprehensive hotel management system designed to streamline the operations of a cabin rental business. It provides a modern, user-friendly interface for managing bookings, cabins, guests, and business analytics.

### Key Features
- 🏨 **Cabin Management**: Add, edit, and delete cabin listings with details like pricing, capacity, and amenities
- 📅 **Booking System**: Handle reservations, check-ins, and check-outs efficiently
- 📊 **Dashboard Analytics**: Track occupancy rates, sales, and other key business metrics
- 👥 **Guest Management**: Maintain guest records and booking history
- 🔒 **User Authentication**: Secure staff accounts with role-based access
- 🌓 **Dark/Light Mode**: Support for both dark and light themes
- ⚙️ **Settings Management**: Customize application settings like booking rules

## Technology Stack

### Frontend Framework
- **React 18**: Modern UI development with functional components and hooks
- **Vite**: Fast and efficient build tooling
- **React Router DOM**: Client-side routing and navigation

### State Management & Data Fetching
- **@tanstack/react-query**: Server state management and caching
- **React Context**: Global application state management
- **React Hook Form**: Form handling and validation

### UI/UX Components
- **Styled Components**: CSS-in-JS styling solution
- **React Icons**: Icon library
- **React Hot Toast**: Toast notifications
- **Recharts**: Data visualization for analytics

### Backend Services
- **Supabase**: Backend-as-a-Service (BaaS) providing:
  - PostgreSQL database
  - Authentication
  - File storage
  - Real-time capabilities

## Project Structure
```
src/
├── assets/          # Static assets (images, icons)
├── context/         # React Context providers
├── features/        # Feature modules
│   ├── authentication/  # Auth-related components
│   ├── bookings/       # Booking management
│   ├── cabins/        # Cabin management
│   ├── dashboard/     # Analytics dashboard
│   └── settings/      # App settings
├── hooks/           # Custom React hooks
├── pages/           # Page components
├── services/        # API and external services
├── styles/          # Global styles
├── ui/             # Reusable UI components
└── utils/           # Utility functions
```

## Getting Started

### Prerequisites
- Node.js 16 or higher
- npm or yarn package manager
- Supabase account for backend services

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/the-wild-oasis.git
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables:
   ```env
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_KEY=your_supabase_anon_key
   ```

4. Start development server:
   ```bash
   npm run dev
   ```

## Documentation Sections

### For Developers
1. [Architecture](architecture.md): System design, component interactions, and data flow
2. [Database](database.md): Database schema, relationships, and queries
3. [Classes](classes.md): Component structure, hooks, and implementation details
4. [Web](web.md): API endpoints, routing, and state management

### For Non-Technical Users
- Start with the Features section above
- Focus on the Functionality descriptions in each document
- Refer to UI/UX sections for interface understanding

## Support and Resources

### Documentation
- [React Documentation](https://react.dev)
- [Supabase Documentation](https://supabase.io/docs)
- [Styled Components Documentation](https://styled-components.com/docs)

### Help and Support
- For technical issues: Open an issue in the GitHub repository
- For usage questions: Contact system administrator
- For feature requests: Submit through the project management system

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is proprietary and confidential.

---

This documentation is maintained by the development team and updated regularly. For questions or suggestions, please contact the documentation team.
