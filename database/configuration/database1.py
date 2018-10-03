import psycopg2
import flask

class Databaseconnection:
    def __init__(self):
            self.connection=psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='admin123'")
            self.connection.autocommit=True
            self.cur= self.connection.cursor()


    def create_tables(self):
        """ create tables in the PostgreSQL database"""

        commands = (
                    """
                    CREATE TABLE IF NOT EXIST MENU (
                        Item_id SERIAL PRIMARY KEY,
                        Item VARCHAR(255) NOT NULL,
                        Price VARCHAR(255) NOT NULL
                    )""")

        self.cur.execute(commands)

    def create_user(self):
        """ create tables in the PostgreSQL database"""

        commands1 = (
                    """
                    CREATE TABLE IF NOT EXIST users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        usermail VARCHAR(255) NOT NULL,
                        userpassword VARCHAR(255) NOT NULL
                    )""")
                    
        self.cur.execute(commands1) 



    def create_userhistory(self):
        """ create tables in the PostgreSQL database"""

        commands2 = (
                    """
                    CREATE TABLE IF NOT EXIST users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        usermail VARCHAR(255) NOT NULL,
                        userpassword VARCHAR(255) NOT NULL
                    )""")
                    
        self.cur.execute(commands2)         
            



                    
               

