import sys

import pandas as pd
import psycopg2


def connect():
    conn = None

    try:
        print('Connecting…')
        conn = psycopg2.connect("dbname=exercises user=postgres password=1234")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("All good, Connection successful!")
    return conn


conn = connect()

a_1 = pd.read_sql_query(
    "SELECT * FROM cd.facilities", conn
)

a_2 = pd.read_sql_query(
    "SELECT name, membercost FROM cd.facilities", conn
)

a_3 = pd.read_sql_query(
    "SELECT * FROM cd.facilities\
    WHERE membercost > 0", conn
)

a_4 = pd.read_sql_query(
    "SELECT * FROM cd.facilities\
    WHERE membercost != 0 \
    AND membercost / monthlymaintenance < 0.02", conn
)

a_5 = pd.read_sql_query(
    "SELECT * FROM cd.facilities\
    WHERE name LIKE '%Tennis%'", conn
)

a_6 = pd.read_sql_query(
    "SELECT * FROM cd.facilities\
    WHERE facid IN (1,5)", conn
)

a_7 = pd.read_sql_query(
    "SELECT * FROM cd.members\
    WHERE joindate >= '2012-09-01'", conn
)

a_8 = pd.read_sql_query(
    "SELECT DISTINCT(surname) FROM cd.members\
    ORDER BY surname\
    LIMIT 10", conn
)

a_9 = pd.read_sql_query(
    "SELECT joindate FROM cd.members\
    ORDER BY joindate DESC\
    LIMIT 1", conn
)

a_10 = pd.read_sql_query(
    "SELECT COUNT(*) FROM cd.facilities\
    WHERE guestcost >= 10", conn
)

a_11 = pd.read_sql_query(
    "SELECT facid, SUM(slots) AS total_slots FROM cd.bookings\
    WHERE starttime BETWEEN '2012-09-01' AND '2012-10-01'\
    GROUP BY facid\
    ORDER BY SUM(slots)", conn
)

a_12 = pd.read_sql_query(
    "SELECT facid, SUM(slots) AS total_slots FROM cd.bookings\
    GROUP BY facid\
    HAVING SUM(slots) > 1000\
    ORDER BY facid", conn
)

a_13 = pd.read_sql_query(
    "SELECT starttime AS start, name FROM cd.bookings\
    INNER JOIN cd.facilities\
    ON bookings.facid = facilities.facid\
    WHERE starttime BETWEEN '2012-09-21' AND '2012-09-22'\
    AND name LIKE 'Tennis%'\
    ORDER BY starttime", conn
)

a_14 = pd.read_sql_query(
    "select starttime AS start_time from cd.bookings\
    INNER JOIN cd.members\
    ON bookings.memid = members.memid\
    WHERE (firstname || ' ' || surname) = 'David Farrell'", conn
)
