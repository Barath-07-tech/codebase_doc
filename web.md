# Web and API Documentation

## User Interface

### Main Pages

1. **Dashboard** (`/pages/Dashboard.jsx`)

   - Overview of current bookings
   - Statistics and charts
   - Quick access to common tasks

2. **Bookings** (`/pages/Bookings.jsx`)

   - List of all bookings
   - Booking status management
   - Filtering and sorting options

3. **Cabins** (`/pages/Cabins.jsx`)

   - Cabin inventory
   - Pricing management
   - Cabin details and images

4. **Users** (`/pages/Users.jsx`)

   - User management
   - Role assignments
   - Profile settings

5. **Settings** (`/pages/Settings.jsx`)
   - System configuration
   - Booking rules
   - Price settings

## Navigation Flow

```plaintext
Login → Dashboard
       │
       ├─→ Bookings ──→ Booking Details
       │
       ├─→ Cabins ────→ Add/Edit Cabin
       │
       ├─→ Users ─────→ User Profile
       │
       └─→ Settings
```

## REST API Endpoints

### Authentication

```plaintext
POST   /api/auth/login       - User login
POST   /api/auth/signup      - Create new user
POST   /api/auth/logout      - User logout
GET    /api/auth/user       - Get current user
PATCH  /api/auth/update-user - Update user data
```

### Bookings

```plaintext
GET    /api/bookings        - List all bookings
GET    /api/bookings/:id    - Get booking details
POST   /api/bookings        - Create booking
PUT    /api/bookings/:id    - Update booking
DELETE /api/bookings/:id    - Delete booking
```

### Cabins

```plaintext
GET    /api/cabins         - List all cabins
GET    /api/cabins/:id     - Get cabin details
POST   /api/cabins         - Create cabin
PUT    /api/cabins/:id     - Update cabin
DELETE /api/cabins/:id     - Delete cabin
```

### Settings

```plaintext
GET    /api/settings       - Get settings
PATCH  /api/settings       - Update settings
```

## UI Components

### Navigation Components

- `MainNav`: Main navigation menu
- `Header`: Top application bar
- `Sidebar`: Side navigation panel

### Data Display

- `Table`: Data grid component
- `DataItem`: Individual data display
- `Pagination`: Page navigation

### Forms

- `Form`: Form container
- `FormRow`: Form field layout
- `Input`: Text input field
- `Select`: Dropdown selection

### Feedback

- `Spinner`: Loading indicator
- `ErrorFallback`: Error display
- `Empty`: Empty state display

## User Workflows

### 1. Booking Management

```plaintext
1. View Bookings List
2. Select Booking
3. View/Edit Details
4. Update Status
5. Save Changes
```

### 2. Cabin Management

```plaintext
1. Access Cabins Page
2. Add/Edit Cabin
3. Set Pricing
4. Upload Images
5. Save Changes
```

### 3. Check-in/Check-out

```plaintext
1. Select Booking
2. Verify Details
3. Collect Payment
4. Update Status
5. Complete Process
```

## Error Handling

### User Feedback

- Clear error messages
- Loading indicators
- Success confirmations

### Form Validation

- Required field checks
- Data format validation
- Real-time feedback

## Security Features

### Authentication

- Protected routes
- Role-based access
- Secure token handling

### Data Protection

- Input sanitization
- HTTPS encryption
- Secure API calls
