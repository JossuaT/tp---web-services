from sqlalchemy import create_engine, text

def send_query_to_db (query, db_string="postgresql://root:root@localhost:5432/test_db"):
    """Send a query to database without results"""
    engine = create_engine(db_string)
    with engine.connect() as connection:
        trans = connection.begin()  
        connection.execute(query)
        trans.commit()

def send_query_to_db_with_results (query, db_string="postgresql://root:root@localhost:5432/test_db"):
    """Send a query to database with results"""
    engine = create_engine(db_string)
    with engine.connect() as connection:
        trans = connection.begin()  
        results = connection.execute(query)
        trans.commit()
    return results

