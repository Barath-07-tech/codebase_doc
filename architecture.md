# System Architecture

## High-Level Overview

The Wild Oasis follows a modern React-based architecture with the following key characteristics:

```plaintext
┌─────────────────────────────────────────┐
│              React Frontend             │
├─────────────┬─────────────┬────────────┤
│  Features   │     UI      │   Hooks    │
└─────┬───────┴──────┬──────┴───────┬────┘
      │              │              │
      ▼              ▼              ▼
┌─────────────┐ ┌──────────┐ ┌──────────┐
│  Services   │ │ Context  │ │  Utils   │
└──────┬──────┘ └────┬─────┘ └────┬─────┘
       │             │             │
       └─────────────┼─────────────┘
                     │
                     ▼
            ┌─────────────────┐
            │    Supabase     │
            └─────────────────┘
```

## Core Components

### 1. Frontend Layer (`/src`)

- **Features Module** (`/features`)

  - Authentication
  - Bookings
  - Cabins
  - Dashboard
  - Settings

- **UI Components** (`/ui`)

  - Reusable interface elements
  - Layout components
  - Form elements
  - Navigation components

- **Context** (`/context`)
  - Dark mode management
  - Global state handling

### 2. Service Layer (`/services`)

- API integrations
- Supabase client
- Authentication services
- Data operations

### 3. Utility Layer (`/utils`)

- Helper functions
- Constants
- Shared utilities

## Data Flow Architecture

```plaintext
User Action → React Component → Custom Hook → Service → Supabase → Database
     ↑                                                              │
     └──────────────────── Response Data ──────────────────────────┘
```

## Key Directories

### Source Structure

```plaintext
src/
├── features/       # Feature-specific components
├── ui/            # Reusable UI components
├── services/      # API and backend services
├── hooks/         # Custom React hooks
├── context/       # React Context providers
├── utils/         # Helper functions
└── styles/        # Global styles
```

## Technical Stack

### Frontend

- React
- Styled Components
- React Query
- React Router
- React Icons

### Backend

- Supabase
  - Authentication
  - Database
  - Storage

### Development Tools

- Vite
- ESLint
- React Hot Toast

## State Management

1. **Local State**: React's useState
2. **Global State**: React Context
3. **Server State**: React Query
4. **Persistent State**: LocalStorage

## Security Architecture

- JWT-based authentication
- Protected routes
- Role-based access control
- Secure API communication

## Performance Considerations

- Code splitting
- Lazy loading
- Optimized images
- Caching strategies
- Real-time updates
