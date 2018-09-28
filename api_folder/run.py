from flask import Flask, Response,abort, request, make_response,jsonify
import json 
from App.utils import search_orders, modify_helper 

app = Flask(__name__) 
#Flaskis a class in module flask that contains extensions that ensure the app runs properly as it shouldand the name is right coz its initial imported application name is different from main so its a place holder


orders = [] 
#we start with an empty list of dictionaries
#our index route

@app.route("/api/v1/")
def index():
    return "Fast Foods App"

#our route for getting all orders
@app.route("/api/v1/orders", methods= ['GET'])
def get_all_orders():
    return make_response(jsonify(orders)),200

#our route for getting anly one order
@app.route("/api/v1/orders/<int:order_id>", methods= ['GET'])
def fetch_one_order(order_id):
    order = search_orders(orders, order_id)
    if order is None:
        abort(404)
    else:
        return make_response(jsonify(order)),200

#our route for placing an order
@app.route("/api/v1/orders", methods= ['POST'])
def place_order():
    data = request.json #picks data sent from json
    if len(orders) == 0:
        order_id = 1   #initializes the first order with order_id 1  
        orders.append({'order_id' : order_id,'user_id': data.get('user_id'),'item_ordered': data.get('item_ordered'),
              'item_quantity':data.get('item_quantity') })
              #adds whatever was sent from postman to orders, using keys from the data object
    else:
        last_dict = orders[len(orders)-1]
        #this picks the last order in the orders list and gets its id which we add onto 1 to auto increment it for the next order
        id = int(last_dict['order_id'])
        new_id = id + 1 
        orders.append({'order_id' : new_id, 'user_id' : data.get('user_id'),'item_ordered' : data.get('item_ordered'), 'item_quantity': data.get('item_quantity')} )
    
    return make_response(jsonify(orders)),201
#modify method.
@app.route("/api/v1/orders/<int:order_id>", methods= ['PUT'])
def modify_order(order_id):
     data = request.json
     if data:
         status = data.get('status')
         response =  modify_helper(orders,order_id,status)
         #modify_helper is a function in utils.py, it helps us modify the order with the status key and value
         return  make_response(jsonify(response)),201

     



if __name__ == '__main__':# checks to c if the whole module runs properly
    app.run(debug=True)
