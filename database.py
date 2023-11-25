from icecream import ic
import psycopg2

class Database:

    def __init__(self):
        self.connection = psycopg2.connect("dbname=app \
                                           user=username \
                                           password=password \
                                           host=IP_or_Name \
                                           port=5432")
        print("Connected to the database.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self.connection:
            self.connection.close()
        print("Connected is closed.")

    def execute_query(self, query, params=None):
        if not self.connection or self.connection.closed != 0:
            self.connect()
        
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        
    def fetch_data(self, query, params=None):
        if not self.connection or self.connection.closed != 0:
            self.connect()
        
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
   
# db = Database()