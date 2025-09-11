# Database Design

## Database System

The Wild Oasis uses Supabase as its backend service, providing a PostgreSQL database with real-time capabilities.

## Entity-Relationship Diagram (ERD)

```plaintext
┌─────────────────┐       ┌──────────────────┐       ┌────────────────┐
│      Users      │       │     Bookings     │       │     Cabins     │
├─────────────────┤       ├──────────────────┤       ├────────────────┤
│ id              │       │ id               │       │ id             │
│ email           │   ┌───┤ userId          │       │ name           │
│ password        │   │   │ cabinId         ├───┐   │ maxCapacity    │
│ fullName        │   │   │ startDate       │   │   │ regularPrice   │
│ avatar          ◄───┘   │ endDate         │   └───┤ discount       │
│ role            │       │ numNights       │       │ description     │
└─────────────────┘       │ numGuests       │       │ image          │
                          │ totalPrice      │       └────────────────┘
                          │ status          │              ▲
                          │ hasBreakfast    │              │
                          │ observations    │       ┌────────────────┐
                          │ isPaid          │       │   Settings     │
                          └──────────────────┘       ├────────────────┤
                                                    │ minBookingLength│
                                                    │ maxBookingLength│
                                                    │ maxGuestsPerBook│
                                                    │ breakfastPrice  │
                                                    └────────────────┘
```

## Tables Description

### 1. Users Table

- **Purpose**: Stores user authentication and profile information
- **Fields**:
  - `id`: Unique identifier (Primary Key)
  - `email`: User's email address (Unique)
  - `password`: Hashed password
  - `fullName`: User's full name
  - `avatar`: URL to user's avatar image
  - `role`: User role (admin/employee)

### 2. Bookings Table

- **Purpose**: Manages cabin booking records
- **Fields**:
  - `id`: Unique identifier (Primary Key)
  - `userId`: Reference to Users table (Foreign Key)
  - `cabinId`: Reference to Cabins table (Foreign Key)
  - `startDate`: Check-in date
  - `endDate`: Check-out date
  - `numNights`: Duration of stay
  - `numGuests`: Number of guests
  - `totalPrice`: Total booking price
  - `status`: Booking status (unconfirmed/checked-in/checked-out)
  - `hasBreakfast`: Breakfast inclusion flag
  - `observations`: Additional notes
  - `isPaid`: Payment status

### 3. Cabins Table

- **Purpose**: Stores cabin information
- **Fields**:
  - `id`: Unique identifier (Primary Key)
  - `name`: Cabin name
  - `maxCapacity`: Maximum guest capacity
  - `regularPrice`: Standard price per night
  - `discount`: Discount amount
  - `description`: Cabin description
  - `image`: Cabin image URL

### 4. Settings Table

- **Purpose**: Stores application configuration
- **Fields**:
  - `minBookingLength`: Minimum nights per booking
  - `maxBookingLength`: Maximum nights per booking
  - `maxGuestsPerBooking`: Maximum guests allowed
  - `breakfastPrice`: Price for breakfast per person

## Relationships

1. **Users → Bookings**

   - One-to-Many relationship
   - One user can have multiple bookings
   - Each booking belongs to one user

2. **Cabins → Bookings**
   - One-to-Many relationship
   - One cabin can have multiple bookings
   - Each booking is for one specific cabin

## Data Access Patterns

### API Services (`/services`)

- `apiAuth.js`: User authentication operations
- `apiBookings.js`: Booking management
- `apiCabins.js`: Cabin operations
- `apiSettings.js`: Settings management

### Key Operations

1. **Bookings**

   - Create new bookings
   - Update booking status
   - Check availability
   - Calculate pricing

2. **Cabins**

   - Manage inventory
   - Update pricing
   - Handle images

3. **Users**
   - Authentication
   - Profile management
   - Role-based access
