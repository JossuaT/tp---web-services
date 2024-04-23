from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_model_and_populate import User_t, Application_t
from populate import create_random_user, create_random_app
from flask_model_and_populate import insert_user_in_db_with_flask, insert_app_in_db_with_flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/test_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Methode GET
@app.route("/create_with_flask")
def create_with_flask():
    for i in range (50):
        insert_user_in_db_with_flask(*create_random_user())
        insert_app_in_db_with_flask(*create_random_app())
    return "Almost 50 user and 50 app have been added to database with flask :)"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
