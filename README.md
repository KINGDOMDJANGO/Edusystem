# Education System

A comprehensive web-based education management system for teachers to compile marks and generate student reports.

## Features

- **Teacher Management**: Add and manage teachers with their subjects
- **Class Management**: Create classes and assign teachers
- **Student Management**: Add students to classes
- **Marks Management**: Record and track student marks for different subjects and exam types
- **Report Generation**: Generate detailed performance reports with charts and statistics
- **Modern UI**: Beautiful, responsive interface built with Bootstrap 5

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://localhost:5000`

## Usage

### Getting Started

1. **Add Teachers**: Start by adding teachers with their subjects
2. **Create Classes**: Create classes and assign teachers to them
3. **Add Students**: Add students to the created classes
4. **Record Marks**: Add marks for students in different subjects
5. **Generate Reports**: View detailed performance reports

### Features Overview

#### Dashboard
- Overview of all statistics
- Quick access to add new entries
- Recent activity display

#### Teachers
- View all teachers
- Add new teachers with subjects
- Edit and delete teachers (coming soon)

#### Classes
- View all classes with assigned teachers
- Add new classes with grade levels
- Edit and delete classes (coming soon)

#### Students
- View all students with their class information
- Add new students to classes
- Edit and delete students (coming soon)

#### Marks
- View all recorded marks
- Add new marks with different exam types
- Calculate percentages automatically
- Edit and delete marks (coming soon)

#### Reports
- Generate class-wise performance reports
- View student rankings
- Performance distribution charts
- Summary statistics

## Database Schema

The system uses SQLite database with the following tables:

- **Teacher**: Teacher information and subjects
- **Class**: Class details with assigned teachers
- **Student**: Student information linked to classes
- **Subject**: Subjects for each class
- **Mark**: Student marks for different subjects and exam types

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap 5
- **Charts**: Chart.js
- **Icons**: Font Awesome

## File Structure

```
education-system/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Dashboard
│   ├── teachers.html     # Teachers listing
│   ├── add_teacher.html  # Add teacher form
│   ├── classes.html      # Classes listing
│   ├── add_class.html    # Add class form
│   ├── students.html     # Students listing
│   ├── add_student.html  # Add student form
│   ├── marks.html        # Marks listing
│   ├── add_mark.html     # Add marks form
│   ├── reports.html      # Reports overview
│   └── class_report.html # Detailed class report
└── education_system.db   # SQLite database (created automatically)
```

## Future Enhancements

- User authentication and authorization
- Edit and delete functionality for all entities
- Bulk import/export of data
- Email notifications
- Advanced analytics and reporting
- Mobile-responsive improvements
- API endpoints for external integrations

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

## License

This project is open source and available under the MIT License. 