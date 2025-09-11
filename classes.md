# Classes and Components

## Component Hierarchy

```plaintext
App
├── AppLayout
│   ├── Header
│   │   ├── HeaderMenu
│   │   └── UserAvatar
│   ├── Sidebar
│   │   └── MainNav
│   └── Main Content
│       └── Feature Components
│
├── Features
│   ├── Authentication
│   ├── Bookings
│   ├── Cabins
│   ├── Check-in-out
│   ├── Dashboard
│   └── Settings
│
└── UI Components
    ├── Forms
    ├── Buttons
    ├── Modals
    └── Tables
```

## Core Components

### 1. Layout Components

```plaintext
AppLayout
├── Provides base structure
├── Manages routing
└── Handles authentication
```

### 2. Feature Modules

#### Authentication (`/features/authentication`)

- **Components**:
  - `LoginForm`: User login interface
  - `SignupForm`: New user registration
  - `UserAvatar`: Display user profile
- **Hooks**:
  - `useLogin`: Handle login logic
  - `useLogout`: Manage logout
  - `useUser`: Access user context

#### Bookings (`/features/bookings`)

- **Components**:
  - `BookingTable`: Display bookings list
  - `BookingDetail`: Show booking information
  - `BookingDataBox`: Present booking statistics
- **Hooks**:
  - `useBooking`: Single booking operations
  - `useBookings`: Multiple bookings management
  - `useDeleteBooking`: Handle booking deletion

#### Cabins (`/features/cabins`)

- **Components**:
  - `CabinTable`: List all cabins
  - `CabinRow`: Individual cabin display
  - `AddCabin`: Cabin creation form
- **Operations**:
  - Create/Edit cabins
  - Manage pricing
  - Handle availability

### 3. UI Components (`/ui`)

#### Forms

- `Form`: Base form component
- `FormRow`: Form field layout
- `Input`: Text input field
- `Select`: Dropdown selection
- `Textarea`: Multi-line input

#### Buttons

- `Button`: Primary action button
- `ButtonGroup`: Button container
- `ButtonIcon`: Icon-only button
- `ButtonText`: Text-only button

#### Feedback

- `Spinner`: Loading indicator
- `SpinnerMini`: Small loading indicator
- `ErrorFallback`: Error display
- `Empty`: Empty state display

## Custom Hooks (`/hooks`)

### State Management

```plaintext
useLocalStorageState
├── Purpose: Persist state in localStorage
└── Usage: Dark mode, user preferences
```

### Navigation

```plaintext
useMoveBack
├── Purpose: Handle navigation history
└── Usage: Back button functionality
```

### UI Interaction

```plaintext
useOutsideClick
├── Purpose: Detect clicks outside elements
└── Usage: Modal closing, dropdown menus
```

## Plain English Explanations

### For Developers

1. **Component Organization**

   - Components are grouped by feature
   - Each feature has its own hooks and utilities
   - UI components are shared across features

2. **State Management**

   - Local state for component-specific data
   - Context for global state
   - Custom hooks for complex logic

3. **Data Flow**
   - Components use hooks for data operations
   - Services handle API communication
   - Context provides global state access

### For Non-Technical Users

1. **User Interface**

   - Clear navigation structure
   - Consistent design patterns
   - Intuitive form handling

2. **Features**

   - Straightforward booking management
   - Easy cabin administration
   - Simple user settings

3. **Data Handling**
   - Automatic data saving
   - Real-time updates
   - Secure information storage
