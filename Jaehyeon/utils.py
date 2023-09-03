import psycopg2
from psycopg2.extensions import connection

def get_connection(
    database="dvdrental",
    host="localhost",
    user="postgres",
    password="1245",
    port="5432"
) -> connection:
    
    return psycopg2.connect(
        database=database,
        host=host,
        user=user,
        password=password,
        port=port
    )


def get_data(con: connection, query: str, num: int=0) -> list[tuple]:
    cur = con.cursor()
    data = None
    try:
        cur.execute(query)
    except Exception as e:
        print(e)
    else:
        if num == 0: data = cur.fetchall()
        else: data = cur.fetchmany(size=num)
    cur.close()
    return data