import psycopg2
from flask import app,make_response, jsonify,abort,request


class Databaseconnection:
    def __init__(self):
            self.connection=psycopg2.connect("dbname='My_fast_food_inc' user='postgres' host='localhost' password='admin123'")
            self.connection.autocommit=True
            self.cur= self.connection.cursor()
            

    def create_tables(self):

        """ create tables in the PostgreSQL database"""

        self.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS MENU (
                        Item_id SERIAL PRIMARY KEY,
                        Item VARCHAR(255) NOT NULL,
                        Price VARCHAR(255) NOT NULL
                    )""")

    
     

       

    def create_user(self):
        """ create tables in the PostgreSQL database"""

        self.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        usermail VARCHAR(255) NOT NULL,
                        userpassword VARCHAR(255) NOT NULL
                    )""")
                    
        



    def create_userhistory(self):
        """ create tables in the PostgreSQL database"""

        self.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS user_history (
                        user_id SERIAL PRIMARY KEY,
                        item_ordered VARCHAR(255) NOT NULL,
                        order_quantity VARCHAR(255) NOT NULL,
                        Order_status VARCHAR(255) NOT NULL
                    )""")
                    
        

    def adminstrator(self):
        """ create tables in the PostgreSQL database"""

        self.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS user_history_admin (
                        user_id SERIAL PRIMARY KEY,
                        item_ordered VARCHAR(255) NOT NULL,
                        order_quantity VARCHAR(255) NOT NULL,
                        Order_status VARCHAR(255) NOT NULL
                    )""")
                    
                   
            



                    
               

