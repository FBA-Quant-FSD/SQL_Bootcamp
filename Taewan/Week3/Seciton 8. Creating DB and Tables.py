import sys

import pandas as pd
import psycopg2


def connect():
    conn = None

    try:
        print('Connecting…')
        conn = psycopg2.connect("dbname=dvdrental user=postgres password=1234")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("All good, Connection successful!")
    return conn


conn = connect()
payment = pd.read_sql_query("SELECT * FROM payment", conn)
film = pd.read_sql_query("SELECT * FROM film", conn)
actor = pd.read_sql_query("SELECT * FROM actor", conn)
film_actor = pd.read_sql_query("SELECT * FROM film_actor", conn)
customer = pd.read_sql_query("SELECT * FROM customer", conn)
address = pd.read_sql_query("SELECT * FROM address", conn)


"""
CREATE TABLE account(
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(250) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	last_login TIMESTAMP
)

CREATE TABLE job(
	job_id SERIAL PRIMARY KEY,
	job_name VARCHAR(200) UNIQUE NOT NULL
)

CREATE TABLE account_job(
	user_id INTEGER REFERENCES account(user_id),
	job_id INTEGER REFERENCES job(job_id),
	hire_date TIMESTAMP
)

INSERT INTO account_job(user_id, job_id, hire_date)
VALUES
(1, 1, CURRENT_TIMESTAMP)

UPDATE account
SET last_login = CURRENT_TIMESTAMP

UPDATE account
SET last_login = created_on

UPDATE account
SET last_login = current_timestamp
RETURNING email, created_on, last_login

DELETE FROM job
WHERE job_name = 'Cowboy'
RETURNING job_id, job_name

CREATE TABLE information(
	info_id SERIAL PRIMARY KEY,
	title VARCHAR(500) NOT NULL,
	person VARCHAR(50) NOT NULL UNIQUE
)

ALTER TABLE information
RENAME TO new_info

ALTER TABLE new_info
RENAME COLUMN person to people

ALTER TABLE new_info
ALTER COLUMN people DROP NOT NULL

ALTER TABLE new_info
DROP COLUMN people

ALTER TABLE new_info
DROP COLUMN IF EXISTS people

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthdate DATE CHECK (birthdate > '1900-01-01'),
	hire_date DATE CHECK (hire_date > birthdate),
	salary INTEGER CHECK (salary > 0)
)

INSERT INTO employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES
('Sammy', 'Smith', '1990-11-03', '2010-10-1', 100)

# SERIAL also counted when query failure
"""
