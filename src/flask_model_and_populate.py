from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from populate import create_random_user, create_random_app

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/test_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User_t(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    age = db.Column(db.Integer())
    email = db.Column(db.String(50))
    job = db.Column(db.String(50))
               
    def __init__(self, id, firstname, lastname, age, email, job):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.job = job


class Application_t(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    appname = db.Column(db.String(50))
    username = db.Column(db.String(50))
    lastconnection = db.Column(db.String(50))
    user_id = db.Column(db.Integer())
              
    def __init__(self, id, appname, username, lastconnection, user_id):
        self.id = id
        self.appname = appname
        self.username = username
        self.lastconnection = lastconnection
        self.user_id = user_id

with app.app_context():
    db.drop_all()
    db.create_all()


def insert_user_in_db_with_flask (id, firstname, lastname, age, email, job):
    try :
        user1= User_t(id, firstname, lastname, age, email, job)
        with app.app_context():
            db.session.add(user1)
            db.session.commit()
    except :
        print(f"ID {id} non-disponible")

def insert_app_in_db_with_flask (id, appname, username, last_connection, user_id):
    try :
        app1= Application_t(id, appname, username, last_connection, user_id)
        with app.app_context():
            db.session.add(app1)
            db.session.commit()
    except :
        print(f"ID {id} non-disponible")