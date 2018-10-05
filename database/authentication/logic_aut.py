import psycopg2
import json
from flask import Flask,app,make_response, jsonify,abort,request

class logic:
    def __init__(self):
        self.connection=psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='admin123'")
        self.connection.autocommit=True
        self.cur= self.connection.cursor()
    
    def register_user(self,user_id,email_address,password,username):

        self.cur.execute("INSERT into users(user_id,email_address,password,username) VALUES(%s,%s,%s,%s)",(user_id,email_address,password,username))
        responseObject = {
                        'status': 'success',
                        'message': 'Successfully registered.'
                                }
        return make_response(jsonify(responseObject)), 201  

    def user_login(self,username,password):
        self.cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
        res = self.cur.fetchone()
        if res[3] == username and res[2] == password:
               
            responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                   
                    }
            return make_response(jsonify(responseObject)), 200    

