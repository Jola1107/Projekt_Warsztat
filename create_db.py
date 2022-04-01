#import library
from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicacteDatabase, Duplicatetable

#info to connect
USER = "postgres"
PASSWORD = "coderslab"
HOST = "127.0.0.1"

# create database
database = "CREATE DATABASE warsztat_db;"
try:
    cnx = connect(user = USER, password = PASSWORD, host = HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(database)
        print("Database warsztat_db created.")
    except Duplicatetable:
        print("Datebase exists")
    cursor.close()
    cnx.close()
except OperationalError:
    print('Connection Error!')

# create table users
table_users = """CREATE TABLE users
(
    id SERIAL,
    username VARCHAR(255),
    hashed_password VARCHAR(80),
    PRIMARY KEY(id)
);
"""
try:
    cnx = connect(user = USER, password = PASSWORD, host = HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(table_users)
        print("Table users created.")
    except Duplicatetable:
        Print("Table exists!")
    cursor.close()
    cnx.close()
except OperationalError:
    print("Connection Error!")
#create table messages
table_messages = """
CREATE TABLE messages
(
    id SERIAL,
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    text VARCHAR(255)
);
"""
try:
    cnx = connect(user = USER, password = PASSWORD, host = HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(table_messages)
        print("Table messages created!")
    except Duplicatetable:
        print("Table exists!")
    cursor.close()
    cnx.close()
except OperationalError:
    print("Connection Error!")

