## Assessment Test 3

#Creating 'students' TABLE
CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	homeroom_number INTEGER,
	phone VARCHAR(50) UNIQUE NOT NULL,
	email VARCHAR(100) UNIQUE,
	graduationyear INTEGER
)


#Creating 'teachers' TABLE
CREATE TABLE teachers(
	teacher_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	homeroom_number INTEGER,
	phone VARCHAR(50) UNIQUE NOT NULL,
	email VARCHAR(100) UNIQUE,
	department VARCHAR(50)
)


#Inserting a student's information
INSERT INTO students(
first_name,last_name,homeroom_number,
phone,graduationyear)
VALUES
('Mark','Watney',5,'777-555-1234',2035)


#Inserting a teacher's information
INSERT INTO teachers(
first_name,last_name,homeroom_number,
phone,email,department)
VALUES
('Jonas','Salk',5,'777-555-4321',
 'jsalk@school.org','Biology')