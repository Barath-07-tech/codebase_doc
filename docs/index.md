# Airline Management System

## Overview
The Airline Management System is a comprehensive Java-based desktop application designed to streamline airline operations, including flight bookings, customer management, and travel documentation.

## Purpose
- Automate airline booking processes
- Manage customer information efficiently
- Handle flight and passenger documentation
- Process booking cancellations and refunds
- Generate real-time reports and analytics

## Key Features
- ✈️ **Customer Management**
  - Add and manage customer profiles
  - Track booking history
  - Maintain customer preferences
  
- 🎫 **Flight Booking**
  - Search available flights
  - Process reservations
  - Generate PNR numbers
  - Issue boarding passes

- 📊 **Flight Information**
  - Real-time flight schedules
  - Pricing details
  - Seat availability
  - Route information
- 🔄 **Journey Management**
  - View booking details
  - Process cancellations
  - Generate refunds
  - Track travel history

## Technology Stack

### Core Technologies
- **Language**: Java
- **GUI Framework**: Java Swing
- **Database**: MySQL
- **Build Tool**: Apache Ant

### Development Tools
- **IDE**: NetBeans
- **Version Control**: Git
- **Database Management**: MySQL Workbench
- **Documentation**: Markdown

## Project Structure
```
src/
├── airlinemanagementsystem/
│   ├── AddCustomer.java     # Customer registration
│   ├── BoardingPass.java    # Boarding pass generation
│   ├── BookFlight.java      # Flight booking
│   ├── Cancel.java          # Cancellation handling
│   ├── ConnDB.java         # Database connectivity
│   ├── FlightInfo.java     # Flight information
│   ├── Home.java           # Main dashboard
│   ├── JourneyDetails.java # Travel information
│   └── Login.java          # User authentication
```

## Target Audience

### For Airline Staff (Non-Technical Users)

- **Counter Staff**: Process bookings and check-ins
- **Customer Service**: Handle cancellations and queries
- **Managers**: Access reports and analytics

### For Developers

- **Java Developers**: Core application logic
- **UI Developers**: Swing interface components
- **Database Administrators**: MySQL schema and queries

## Documentation Sections

1. [System Architecture](architecture.md)
   - System design
   - Component interaction
   - Data flow diagrams

2. [Database Design](database.md)
   - Table structures
   - ERD diagrams
   - Query patterns

3. [Classes & Components](classes.md)
   - Class hierarchy
   - UI components
   - Business logic

4. [UI Flow](web.md)
   - Screen navigation
   - User interactions
   - Interface guidelines

## Getting Started

### Prerequisites
- Java Development Kit (JDK) 8+
- MySQL Server 5.7+
- NetBeans IDE (recommended)
- Git (optional)

### Installation Steps
1. Clone the repository
2. Open project in NetBeans
3. Configure database connection
4. Build and run the application

## Documentation Maintenance
This documentation is maintained as part of the codebase and should be updated whenever:
- New features are added
- Existing features are modified
- Bug fixes affect behavior
- Database schema changes

## Quick Start

1. Log in to the system
2. Navigate through the dashboard
3. Access cabin management
4. Handle bookings
5. Configure settings

## Key Features

- User authentication and authorization
- Cabin inventory management
- Booking system
- Check-in/check-out handling
- Dark/light mode support
- Responsive design
- Real-time updates
- Statistical dashboard
