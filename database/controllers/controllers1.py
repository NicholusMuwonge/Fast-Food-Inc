import psycopg2
from flask import Flask


class methods:
    def __init__(self):
        self.connection=psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='admin123'")
        self.connection.autocommit=True
        self.cur= self.connection.cursor()

    def add_item(self):
        """INSERT ITEMS INTO TABLES"""
        post="""INSERT INTO Menu(item) VALUES(%s)"""
        self.cur.execute(post)

    def     

