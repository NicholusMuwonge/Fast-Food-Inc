import psycopg2
import json
from flask import Flask,app,make_response, jsonify,abort,request


class methods:
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


    def place_order(self,user_id,order_id,item_id,item_name,item_quantity,price,status):
        self.cur.execute("INSERT INTO orders(order_id,user_id,item_id,item_name,item_quantity,price,status) VALUES(%s,%s,%s,%s,%s,%s,%s)",(order_id,user_id,item_id,item_name,item_quantity,price,status))
        responseObject = {'message':'order placed'}       
        return make_response(jsonify(responseObject)),201 #created
       
                
        
    def get_all_orders(self):

            self.cur.execute("SELECT * FROM orders")
            orders = self.cur.fetchall()
            responseObject = {
			'order': 'order' , 'message':'order retrieved'
                    }
            for order in orders:
                return make_response(jsonify(order,responseObject)),200
  
    def get_a_specific_order(self,order_id):
            self.cur.execute("SELECT * FROM orders WHERE order_id =%s ",(order_id,))
            order_id = self.cur.fetchone()
            responseObject = {
			'order': 'order' , 'message':'order retrieved'
                    }
                    
            return make_response(jsonify(responseObject)),200       
        
     
       

    def update_order_status(self,order_id):
        try:
            data = request.json
            status = data.get('status')
            self.cur.execute("UPDATE orders SET status=%s WHERE order_id=%s",(status,order_id))
            responseObject = {
                        'status': status,
			'message': 'updated successfully'
                    }
            return make_response(jsonify(responseObject)),201
                    
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Faild to retrieve specific order'
                }
            return make_response(jsonify(responseObject)), 401 #unauthorized     
        
         

    def get_menu(self):
        self.cur.execute("SELECT * FROM menu")
        menu = self.cur.fetchall()
           
        responseObject = {
			'message':'menu retrieved'
                    }
        for item in menu:
            return make_response(jsonify(item,responseObject)),200
                      
        

    def add_food_item_to_menu(self,item_id,item_name,item_price):
        self.cur.execute("INSERT INTO menu(item_id,item_name,price) VALUES(%s,%s,%s)",(item_id,item_name,item_price))
        responseObject = {'item added': item_name ,'item_price': item_price ,'message':'food item added' }            
        return make_response(jsonify(responseObject)),201
        

    def get_order_history(self,user_id):
        try:
            self.cur.execute("SELECT * FROM orders WHERE user_id =%s",(user_id,))
            history = self.cur.fetchall()
            responseObject = { 'message':'order history retrieved successfully'}
            for order in history:
                return make_response(jsonify(order,responseObject)),200
                      
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Failed to retrieve order history '
                }
            return make_response(jsonify(responseObject)), 401 #unauthorized 
    
    


        

