# Airline Management System

## Purpose
The Airline Management System is a comprehensive desktop application designed to streamline and automate various aspects of airline operations. It provides an intuitive interface for managing flights, passengers, bookings, and other essential airline services.

## Key Features
1. **User Authentication**
   - Secure login system for staff members
   - Role-based access control
   - Password encryption

2. **Customer Management**
   - Add new customer profiles
   - Store essential customer information
   - Validate customer identity through Aadhar
   - Manage customer records

3. **Flight Operations**
   - View flight schedules and details
   - Check flight availability
   - Manage flight routes
   - Update flight status

4. **Booking Management**
   - Create new flight bookings
   - Generate unique PNR numbers
   - Select seats and preferences
   - Process ticket cancellations
   - Generate boarding passes

## Technology Stack

### Core Technologies
- **Java SE**: Primary programming language
- **Swing/AWT**: GUI framework for desktop interface
- **MySQL**: Database management system
- **JDBC**: Database connectivity
- **DbUtils**: Database utility library

### Development Tools
- **NetBeans IDE**: Primary development environment
- **Git**: Version control system
- **Maven**: Build automation tool (optional)

## Getting Started

### System Requirements
1. **Hardware Requirements**
   - Processor: 2 GHz or higher
   - RAM: 4 GB minimum
   - Storage: 500 MB free space

2. **Software Requirements**
   - Java Runtime Environment (JRE) 8 or higher
   - MySQL Server 5.7 or higher
   - Windows/Linux/macOS operating system

### Installation Steps
1. Install Java Runtime Environment
2. Set up MySQL Server
3. Import database schema
4. Configure connection settings
5. Launch the application

## Documentation Sections

### [Architecture Documentation](architecture.md)
- System design and components
- Flow diagrams
- Integration points
- Security architecture

### [Database Documentation](database.md)
- Database schema
- Entity relationships
- Table structures
- Query patterns

### [Class Documentation](classes.md)
- Class hierarchies
- UML diagrams
- Method descriptions
- Code examples

### [Web Documentation](web.md)
- Web interfaces
- API endpoints
- Navigation flows
- Integration guides

## Common Terms and Definitions

### Business Terms
- **PNR (Passenger Name Record)**: A unique identifier for each booking
- **Aadhar**: India's unique identification number
- **Boarding Pass**: Document allowing passenger to board aircraft

### Technical Terms
- **JFrame**: Main window container in Java Swing
- **ActionListener**: Interface for handling user actions
- **JDBC**: Java Database Connectivity API
- **ResultSet**: Database query results container

## For Developers

### Project Structure
```
AirlineManagementSystem/
├── src/
│   └── airlinemanagementsystem/
│       ├── Login.java         # Authentication
│       ├── Home.java         # Main dashboard
│       ├── AddCustomer.java  # Customer registration
│       ├── BookFlight.java   # Flight booking
│       ├── Cancel.java       # Cancellation handling
│       └── ...
├── nbproject/                # NetBeans config
└── build.xml                 # Build script
```

### Key Classes Overview
- **Login**: Entry point and authentication
- **Home**: Main navigation dashboard
- **AddCustomer**: Customer registration interface
- **BookFlight**: Flight booking management
- **ConnDB**: Database connection handler

## For Non-Technical Users

### Basic Operations
1. **Starting the System**
   - Launch the application
   - Enter login credentials
   - Access the main dashboard

2. **Adding a New Customer**
   - Click "Add Customer Details"
   - Fill in required information
   - Save the customer profile

3. **Booking a Flight**
   - Select "Book Flight"
   - Enter passenger details
   - Choose flight and date
   - Confirm booking

4. **Managing Bookings**
   - View journey details
   - Generate boarding passes
   - Process cancellations

### Tips and Best Practices
1. Always verify customer information
2. Double-check flight details before booking
3. Keep PNR numbers for reference
4. Regularly update passenger information

## Support and Resources
- Technical documentation in respective sections
- Database backup procedures
- Error handling guidelines
- Troubleshooting steps

## Version Information
- Current Version: 1.0
- Last Updated: October 2025
- Supported Java Versions: 8+
- Supported MySQL Versions: 5.7+
