# The Wild Oasis Hotel Management System

## Purpose
The Wild Oasis is a comprehensive hotel management system designed to streamline operations for boutique hotels. This modern web application helps hotel staff efficiently manage cabin bookings, guest information, and daily operations through an intuitive dashboard interface.

## Target Audience
### Hotel Staff (Non-Technical Users)
- Reception staff managing bookings and check-ins
- Managers monitoring performance metrics
- Administrative staff handling cabin management
- Support staff updating hotel settings

### Developers
- Frontend developers maintaining and extending the application
- Backend developers working with Supabase integration
- DevOps engineers handling deployment and maintenance
- QA engineers testing new features

## Key Features
- 🏠 **Cabin Management**: Add, edit, and remove cabin listings with photos and detailed information
- 📅 **Booking System**: Handle reservations and check-in/check-out processes
- 👥 **Guest Management**: Track guest information and booking history
- 📊 **Dashboard**: Real-time statistics and booking analytics
- ⚙️ **Settings Management**: Customize hotel settings and pricing
- 🔐 **User Authentication**: Secure staff access with role-based permissions

## Technology Stack
### Frontend
- **React 18**: Core framework for building the user interface
- **Styled Components**: For component-level styling with dynamic theming
- **React Query**: Data fetching and state management
- **React Hook Form**: Form handling and validation
- **Recharts**: Data visualization for analytics
- **React Hot Toast**: User notifications
- **React Icons**: Icon library

### Backend & Database
- **Supabase**: Backend as a Service (BaaS) providing:
  - PostgreSQL database
  - Authentication
  - File storage
  - Real-time subscriptions

## Project Structure
```
src/
├── features/          # Feature-specific components and logic
│   ├── authentication/  # Login, signup, user management
│   ├── bookings/       # Booking-related features
│   ├── cabins/         # Cabin management
│   ├── dashboard/      # Analytics and statistics
│   └── settings/       # Application settings
├── services/         # API and external service integrations
├── hooks/            # Custom React hooks
├── ui/              # Reusable UI components
├── utils/           # Helper functions and constants
├── styles/          # Global styles and theme
└── context/         # React Context providers
```

## Getting Started
1. Clone the repository
2. Install dependencies: `npm install`
3. Set up environment variables:
   ```
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_KEY=your_supabase_anon_key
   ```
4. Run development server: `npm run dev`

## Documentation Sections
- [System Architecture](architecture.md): Detailed system design, component interactions, and data flow diagrams
- [Database Schema](database.md): Data structure, relationships, and Supabase integration details
- [Component Documentation](classes.md): In-depth documentation of components, hooks, and utilities
- [Web Interface](web.md): API endpoints, pages structure, and navigation flow

## Development Guidelines
- Use consistent code formatting (ESLint and Prettier configured)
- Follow component-based architecture
- Implement proper error handling
- Write meaningful commit messages
- Keep dependencies updated

## Contribution
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support
For technical support or feature requests, please create an issue in the repository.
