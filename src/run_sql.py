from flask import Flask
from sqlalchemy import create_engine, text
from populate import create_random_user, insert_user_in_db
from populate import create_random_app, insert_app_in_db
from connection_to_DB import send_query_to_db

db_string = "postgresql://root:root@localhost:5432/test_db"
engine = create_engine(db_string)


#Création des deux tables (requêtes + exec)
create_table_user_statement = text("""
CREATE TABLE IF NOT EXISTS user_table
    (id int PRIMARY KEY, firstname text, lastname text, age int, email text, job text);
""")
create_table_app_statement = text("""
    CREATE TABLE IF NOT EXISTS application_table
        (id int PRIMARY KEY, appname text, username text, lastconnection text, user_id int);
""")

send_query_to_db(create_table_user_statement)
send_query_to_db(create_table_app_statement)



app = Flask(__name__)

# Populate avec la methode GET
@app.route("/create_with_sql")
def create_sql():
    #Insertion de données dans les tables
    for i in range (0,50):
        insert_user_in_db(*create_random_user())
        insert_app_in_db(*create_random_app())
    return "Almost 50 user and 50 app have been added to database with sql :)"

# route /home 
@app.route('/print_user_table')
def print_table():
    res = []
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM user_table"))
        connection.commit()
        data = []
        for row in result :
            user ={
                "id":row[0],
                "fisrtname":row[1],
                "lastname":row[2],
                "age":row[3],
                "email":row[4],
                "job":row[5]
            }
            data.append(user)          
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)