# College Management
The Student Information Management System is a desktop-based application built using Python and Tkinter. It is designed to manage student data efficiently, including storing, displaying, updating, and deleting student records. The application features a user-friendly interface and supports various functionalities such as adding new student records, validating data, and performing CRUD operations (Create, Read, Update, Delete).

## Features
- Student Record Management: Add, view, update, and delete student information such as name, father’s name, mother’s name, address, mobile number, email ID, date of birth, and gender.
- Data Validation:
  - Mobile Number: Validates that the mobile number is numeric, 10 digits long, and starts with specific digits (6, 7, 8, or 9).
  - Email: Ensures that the email is in the correct format using regular expressions.
  - Date of Birth: Verifies that the date of birth is in the correct format and represents a valid date.
- GUI Interface: Developed with Tkinter for an intuitive graphical user interface that allows easy interaction with the system.
- Database Interaction: Data is stored and retrieved using a backend database (Std_info_BackEnd module), allowing persistent storage for student records.
- CRUD Operations:
  - Add Student: Adds a new student to the database.
  - Update Student: Modifies the details of an existing student.
  - Delete Student: Removes a student record from the system.
  - Search Student: Searches for a student based on various criteria (e.g., name, ID, mobile number).
- Display All Records: Displays all student records in a list.

## Technologies Used
- Python: The core programming language used to develop the system.
- Tkinter: A Python library for creating graphical user interfaces.
- Regular Expressions (re): Used to validate email and mobile number formats.
- Datetime: Utilized to validate the date of birth format and ensure it is a valid date.
- Std_info_BackEnd: The backend module responsible for database interaction (such as insert, update, delete, and search operations).
