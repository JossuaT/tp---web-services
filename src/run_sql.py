from sqlalchemy import create_engine

db_string = "postgresql://root:root@localhost:5432/db"

engine = create_engine(db_string)
connection = engine.connect()

# Create
#connection.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
#connection.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")