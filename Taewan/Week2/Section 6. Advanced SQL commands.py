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

# challenge 1
c_1 = pd.read_sql_query(
    "SELECT DISTINCT TO_CHAR(payment_date, 'Month') FROM payment", conn
)

c_2 = pd.read_sql_query(
    "SELECT COUNT(*) FROM payment\
    WHERE EXTRACT(DOW FROM payment_date) = 1", conn
)

df_1 = pd.read_sql_query(
    "SELECT ROUND(rental_rate / replacement_cost, 4)*100 AS result_percent FROM film", conn
)

df_2 = pd.read_sql_query(
    "SELECT LENGTH(first_name) FROM customer", conn
)

df_3 = pd.read_sql_query(
    "SELECT first_name || ' ' || last_name FROM customer", conn
)

df_4 = pd.read_sql_query(
    "SELECT upper(first_name) || ' ' || last_name AS full_name FROM customer", conn
)

df_5 = pd.read_sql_query(
    "SELECT LOWER(LEFT(first_name, 1)) || LOWER(last_name) || '@gmail.com' AS email FROM customer", conn
)

df_6 = pd.read_sql_query(
    "SELECT title, rental_rate FROM film\
    WHERE rental_rate >\
    (SELECT AVG(rental_rate) FROM film)", conn
)

df_7 = pd.read_sql_query(
    "SELECT * FROM rental\
    WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30'", conn
)

df_8 = pd.read_sql_query(
    "SELECT inventory.film_id FROM rental\
    INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id\
    WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30'", conn
)

df_9 = pd.read_sql_query(
    "SELECT film_id, title FROM film\
    WHERE film_id IN\
    (SELECT inventory.film_id FROM rental\
    INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id\
    WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30')\
    ORDER BY film_id", conn
)

df_10 = pd.read_sql_query(
    "SELECT first_name, last_name FROM customer AS c\
    WHERE EXISTS\
    (SELECT * FROM payment AS p\
    WHERE p.customer_id = c.customer_id\
    AND amount > 11)", conn
)

df_11 = pd.read_sql_query(
    "SELECT * FROM payment AS p\
    WHERE p.customer_id = customer.customer_id\
    AND amount > 11", conn
)

df_12 = pd.read_sql_query(
    "SELECT f1.title, f2.title, f1.length\
    FROM film AS f1\
    INNER JOIN film AS f2\
    ON f1.length = f2.length", conn
)

df_13 = pd.read_sql_query(
    "SELECT f1.title, f2.title, f1.length\
    FROM film AS f1\
    INNER JOIN film AS f2\
    ON f1.length != f2.length\
    AND f1.length = f2.length", conn
)
