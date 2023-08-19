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

a_1 = pd.read_sql_query(
    "SELECT customer_id FROM payment \
    WHERE staff_id=2 \
    GROUP BY customer_id \
    HAVING SUM(amount) > 110", conn
)

a_2 = pd.read_sql_query(
    "SELECT COUNT(*) FROM film \
    WHERE title LIKE 'J%'", conn
)

a_3 = pd.read_sql_query(
    "SELECT first_name, last_name FROM customer \
    WHERE first_name LIKE 'E%' \
    AND address_id < 500\
    ORDER BY customer_id DESC\
    LIMIT 1", conn
)
