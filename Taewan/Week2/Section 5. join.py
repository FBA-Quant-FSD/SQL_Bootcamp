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
    "SELECT SUM(amount) AS net_revenue FROM payment", conn
)

df_2 = pd.read_sql_query(
    "SELECT COUNT(*) AS num_transaction FROM payment", conn
)

df_3 = pd.read_sql_query(
    "SELECT customer_id, SUM(amount) AS total_spent FROM payment\
    GROUP BY customer_id", conn
)

df_4 = pd.read_sql_query(
    "SELECT customer_id, SUM(amount) AS total_spent FROM payment\
    GROUP BY customer_id \
    HAVING SUM(amount) > 100", conn
)

df_5 = pd.read_sql_query(
    "SELECT customer_id, amount AS new_name FROM payment\
    WHERE amount > 2", conn
)

df_6 = pd.read_sql_query(
    "SELECT * FROM payment\
    INNER JOIN customer\
    ON payment.customer_id = customer.customer_id", conn
)

df_7 = pd.read_sql_query(
    "SELECT payment_id, payment.customer_id, first_name FROM payment\
    INNER JOIN customer\
    ON payment.customer_id = customer.customer_id", conn
)

df_8 = pd.read_sql_query(
    "SELECT * FROM customer\
    FULL OUTER JOIN payment\
    ON customer.customer_id = payment.customer_id", conn
)

df_9 = pd.read_sql_query(
    "SELECT film.film_id, title, inventory_id, store_id FROM film\
    LEFT JOIN inventory ON\
    inventory.film_id = film.film_id\
    WHERE inventory.film_id IS NULL", conn
)

# challenge 1
c_1 = pd.read_sql_query(
    "SELECT district, email FROM address\
    INNER JOIN customer ON\
    address.address_id = customer.address_id\
    WHERE district = 'California'", conn
)

c_2 = pd.read_sql_query(
    "SELECT title, first_name, last_name FROM actor\
    INNER JOIN film_actor ON\
    actor.actor_id = film_actor.actor_id\
    INNER JOIN film ON\
    film_actor.film_id = film.film_id\
    WHERE first_name = 'Nick'\
    AND last_name = 'Wahlberg'", conn
)
