"""
This file contains function to create random user and app
    and function to insert these objects in the database.
"""

from faker import Faker
from random import randint, choice
from sqlalchemy import text
from datetime import datetime
from connection_to_DB import send_query_to_db

fake = Faker()

db_string = "postgresql://root:root@localhost:5432/test_db"

def create_random_user ():
    id = randint(1,9999)
    firstname = fake.first_name()
    lastname = fake.last_name()
    age = randint(1,100)
    email = fake.email()
    job = fake.job()
    return id, firstname, lastname, age, email, job

def insert_user_in_db(id, firstname, lastname, age, email, job):
    try :
        insert_statement = text(f"""
            INSERT INTO user_table (id, firstname, lastname, age, email, job) 
            VALUES ({id}, '{firstname}', '{lastname}', {age}, '{email}', '{job}')
        """)
        send_query_to_db (insert_statement, db_string)
    except :
        print(f"ID {id} non-disponible")


def create_random_app ():
    app_list = ["Instagram", "Snapchat", "TikTok", "Twitter", "LinkedIn",
                "Pinterest", "Youtube", "Facebook", "Netflix", "WhatsApp",
                "AirBNB", "Duolingo", "Vivino", "Uber", "Moodle", "Teams"]
    id = randint(1,9999)
    appname = choice(app_list)
    username = fake.user_name()
    last_connection = datetime.now()
    user_id = randint(1,9999)
    return id, appname, username, last_connection, user_id


def insert_app_in_db(id, appname, username, last_connection, user_id):
    try :
        insert_statement = text(f"""
            INSERT INTO application_table (id, appname, username, lastconnection, user_id) 
            VALUES ({id}, '{appname}', '{username}', '{last_connection}', {user_id})
        """)
        send_query_to_db(insert_statement)
    except :
        print(f"ID {id} non-disponible")
