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

df_1 = pd.read_sql_query(
    "SELECT customer_id,\
    CASE\
        WHEN (customer_id <= 100) THEN 'Premium'\
        WHEN (customer_id BETWEEN 100 and 200) THEN 'Plus'\
        ELSE  'Normal'\
    END AS customer_class\
    FROM customer", conn
)

df_2 = pd.read_sql_query(
    "SELECT customer_id,\
    CASE customer_id\
        WHEN 2 THEN 'Winner'\
        WHEN 5 THEN 'Second Place'\
        ELSE  'Normal'\
    END AS raffle_results\
    FROM customer", conn
)

df_3 = pd.read_sql_query(
    "SELECT rental_rate,\
    CASE rental_rate\
        WHEN 0.99 THEN 1\
        ELSE  0\
    END\
    FROM film", conn
)

df_4 = pd.read_sql_query(
    "SELECT\
    SUM(CASE rental_rate\
        WHEN 0.99 THEN 1\
        ELSE  0\
    END) AS number_of_bargains\
    FROM film", conn
)

df_5 = pd.read_sql_query(
    "SELECT CAST('5' AS INTEGER) AS new_int", conn
)

df_6 = pd.read_sql_query(
    "SELECT '10'::INTEGER", conn
)

df_7 = pd.read_sql_query(
    "SELECT CAST(inventory_id AS VARCHAR) from rental", conn
)

df_8 = pd.read_sql_query(
    "SELECT CHAR_LENGTH(CAST(inventory_id AS VARCHAR)) from rental", conn
)

"""
CREATE TABLE depts(
	first_name VARCHAR(50),
	department VARCHAR(50)
)

INSERT INTO depts(
	first_name, department
)
VALUES
('Vinton', 'A'),
('Lauren', 'A'),
('Claire', 'B');

SELECT (
	SUM(CASE WHEN department = 'A' THEN 1 ELSE 0 END) /
	NULLIF (
	SUM(CASE WHEN department = 'B' THEN 1 ELSE 0 END),0)
) AS department_ratio
FROM depts

CREATE VIEW customer_info AS
SELECT first_name, last_name, address FROM customer
INNER JOIN address
ON customer.address_id = address.address_id

CREATE OR REPLACE VIEW customer_info AS
SELECT first_name, last_name, address, district FROM customer
INNER JOIN address
ON customer.address_id = address.address_id

DROP VIEW IF EXISTS customer_info

ALTER VIEW customer_info RENAME TO customer_info_2
"""


df_9 = pd.read_sql_query(
    "SELECT * FROM customer_info", conn
)
