import psycopg2
import logging
# from config import config


class MyDatabase:
    # To connect database and instantiate cursor
    def __init__(self, db="db1", user="postgres"):
        try:
            # params = config()
            self.conn = psycopg2.connect(database=db, user=user, password='root', port='5433')
            # self.conn = psycopg2.connect(**params)
            self.cur = self.conn.cursor()
            logging.info("Database Connected")
        except:
            logging.error("Unable to connect the database")

    # To query the database
    def query(self, query):
        try:
            self.cur.execute(query)
            records = self.cur.fetchall()
            logging.info(f"Query executed - {query}")
            return records
        except:
            logging.error(f"Query failed - {query}")

    # To update in the db
    def update(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            logging.info(f"Update done - {query}")
        except:
            logging.error(f"Update failed - {query}")

    # To close the connection
    def close(self):
        try:
            self.cur.close()
            self.conn.close()
            logging.info("Cursor and Connection Closed")
        except:
            logging.error("Unable to close cursor and connection")

