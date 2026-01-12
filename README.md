# Student-demo
This is my first Git Repository
# Student Management System

A simple Student Management System built using Python and SQLAlchemy.

## Features
- Add student
- View students
- SQLite database
- Beginner-friendly project
  
**Student Table Schema**

| Column   | Type    | Meaning                  |
| -------- | ------- | ------------------------ |
| `id`     | INT     | Student ID (Primary Key) |
| `name`   | VARCHAR | Student name             |
| `age`    | INT     | Student age              |
| `course` | VARCHAR | Course name              |

**API Endpoints**

| Method   | Endpoint         | Purpose           |
| -------- | ---------------- | ----------------- |
| `POST`   | `/students`      | Add new student   |
| `GET`    | `/students`      | Get all students  |
| `GET`    | `/students/{id}` | Get student by ID |
| `PUT`    | `/students/{id}` | Update student    |
| `DELETE` | `/students/{id}` | Delete student

**Example Request (Add Student)**
POST /STU
{
  "name": "Riya Patil",
  "age": "21",
  "course": "DSA"
}

