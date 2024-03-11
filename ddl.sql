CREATE DATABASE University;

CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
)