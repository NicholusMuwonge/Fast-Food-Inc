import psycopg2
import json, datetime, jwt
from flask import make_response, jsonify,abort,request
from application import app

class DatabaseConnection():

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                " dbname='fast-foods-db' user='postgres' host='localhost' password='password' port='5432' ")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Cannot connect to database")
    
    def encode_auth_token(self,user_id):     
        secret_key = app.config.get('SECRET_KEY')
        payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=6000),'iat': datetime.datetime.utcnow(),'sub': user_id }
        return jwt.encode(payload,secret_key,algorithm='HS256')
        
    def decode_auth_token(self,auth_token):
        secret_key = app.config.get('SECRET_KEY')
        payload = jwt.decode(auth_token, secret_key)
        return payload['sub']

    def register_user(self,user_id,email_address,password,username):
        if self.cursor.execute("INSERT into users(user_id,email_address,password,username) VALUES(%s,%s,%s,%s)",(user_id,email_address,password,username)):
 
            if self.cursor.execute("SELECT user_id FROM users WHERE username=%s AND password=%s",(username,password)):
                result = user_id_sql.fetchone()
                user_id = result[0]
                auth_token = encode_auth_token(user_id)
            responseObject = {
                        'status': 'success',
                        'message': 'Successfully registered.',
                        'auth-token': auth_token.decode() }
            return make_response(jsonify(responseObject)), 201

        else:
            responseObject = {
                        'status': 'fail',
                        'message': 'Some error occurred. Please try again.'
                                }
            return make_response(jsonify(responseObject)), 500
 
        
    def user_login(self,username,password):  
        if self.cursor.execute("SELECT FROM * users WHERE username=%s AND password=%s",(username,password)):
            res = self.cursor.fetchone()
            if res[3] == username and res[2] == password:
                user_id = res[0]
                auth_token = encode_auth_token(user_id)
                if auth_token:
                    responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                'status': 'Login failed',
                'message': 'Try again'
                }
            return make_response(jsonify(responseObject)), 500
            
    def place_order(self,order_id,user_id,item_id,item_name,item_quantity,price,status):

        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                if self.cursor.execute("INSERT INTO orders(order_id,user_id,item_id,item_name,item_quantity,price,status) VALUES(%s,%s,%s,%s,%s,%s,%s)",(order_id,user_id,item_id,item_name,item_quantity,price,status)):
                    responseObject = {
                        'message':'order placed',
                        'status':'success'
                    }
                    return make_response(jsonify(responseObject)),201 #created
                else:
                    responseObject ={'status': 'fail',
                                     'message': 'Query failed'}
                    return make_response(jsonify(responseObject)),401 #unauthorized
                     
                
        
    def qet_all_orders(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                self.cursor.execute("SELECT * FROM orders")
                orders = self.cursor.fetchall()
                responseObject = {
			        'message':'all orders retrieved',	
                    'status':'success'
                    }
                for order in orders:
                    return make_response(jsonify(order,responseObject)),200
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Faild to retrieve orders'
                }
            return make_response(jsonify(responseObject)), 401 #unauthorized        
        
        

    def qet_a_specific_order(self,order_id):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                self.cursor.execute("SELECT * FROM orders WHERE order_id =%s "(order_id,))
                order = self.cursor.fetchone()
                responseObject = {
	        		'order': order , 'message':'order retrieved', 'status':'success'}                  
                    
                return make_response(jsonify(responseObject)),200
                    
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Faild to retrieve specific order'
                }
            return make_response(jsonify(responseObject)), 404        
        
     
       

    def update_order_status(self,orderId):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                data = request.json
                status = data.get('status')
                self.cursor.execute("UPDATE orders SET status=%s WHERE order_id=%s",(status,orderId))
                responseObject = {
                        'status': status ,
			            'message': 'updated successfully'
                    }
                return make_response(jsonify(responseObject)),201
                    
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Faild to retrieve specific order'
                }
            return make_response(jsonify(responseObject)), 401 #unauthorized     
        
         

    def qet_menu(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                if self.cursor.execute("SELECT * FROM menu"):
                    menu = self.cursor.fetchall()
                    responseObject = {
                    'status':'success',
			        'message':'menu retrieved'
                    }
                    return make_response(jsonify(responseObject)),200  
                #for item in menu:
                    #return make_response(jsonify(item)),200
                     
                  
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Faild to retrieve menu'
                }
            return make_response(jsonify(responseObject)), 404    
        

    def add_food_item_to_menu(self,item_name,item_price):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                self.cursor.execute("INSERT INTO menu(item_name,price) VALUES(%s,%s)",(item_name,item_price))  
                responseObject = { 'item added': item_name ,'item_price': item_price ,'auth_token': auth_token.decode(), 'message':'food item added' }            
                return make_response(jsonify(responseObject)),201
                                  
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Faild to add food item to menu'
                }
            return make_response(jsonify(responseObject)), 401 #unauthorized   

    def get_order_history(self,user_id):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                self.cursor.execute("SELECT * FROM orders WHERE user_id =%s",(user_id,))
                history = self.cursor.fetchall()
                responseObject = {'auth_token': auth_token.decode() , 'message':'order history retrieved successfully'}
                for order in history:
                    return make_response(jsonify(order,responseObject)),200
                      
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Failed to retrieve order history '
                }
            return make_response(jsonify(responseObject)), 401 #unauthorized 
    
    
    
    
        
         
    
  