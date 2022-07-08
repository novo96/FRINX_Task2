import psycopg2
import datetime
import os
from dotenv import load_dotenv

#This script contains functions for connecting, inserting to and reading from the db

load_dotenv()

def connect():
    conn = psycopg2.connect(
            host = 'db',
            database = 'postgres',
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD")
            )
    return conn

def get_cur(conn):
    cur = conn.cursor()
    return cur

def create_table(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS history (date VARCHAR, time VARCHAR, command VARCHAR, output VARCHAR, color VARCHAR);")

def insert(conn, cur, command, output, color):
    cur.execute("INSERT INTO history (date, time, command, output, color) VALUES (%s, %s, %s, %s, %s)", 
    (str(datetime.date.today()), datetime.datetime.now().strftime("%H:%M:%S"), command.upper(), output, color))

    conn.commit()

def read(cur):
    cur.execute("SELECT * FROM history")
    rows = cur.fetchall()
    if not len(rows):
        print("Empty")
    else:
        for row in rows:
            if row[4] == "green":
                print(row[0], row[1], row[2], f"\033[92m{row[3]}\033[00m")
            else:
                print(row[0], row[1], row[2], f"\033[91m{row[3]}\033[00m")

def close(conn, cur):
    cur.close()
    conn.close()

if __name__ == '__main__':
    conn = connect()
    cur = get_cur(conn)
    read(cur)
    close(conn, cur)

