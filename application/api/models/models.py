import json 
 
from application.api.controllers import utils
from flask import Flask, make_response, jsonify,abort,request 

#we start with an empty list of dictionaries
orders = []

class models():
        
             

        def get_all_orders():
            return make_response(jsonify(orders)),200

         
        def fetch_one_order(self,order_id):
            order = utils.search_orders(orders, order_id)
            if order is None:
                abort(404)
            else:
                return make_response(jsonify(order)),200

        
        def place_order():
            data = request.json 
            if len(orders) == 0:
                order_id = 1     
                orders.append({'order_id' : order_id,'user_id': data.get('user_id'),'item_ordered': data.get('item_ordered'),
                      'item_quantity':data.get('item_quantity') })
                      
            else:
                last_dict = orders[len(orders)-1]
                #this picks the last order in the orders list and gets its id which we add onto 1 to auto increment it
                #for the next order
                id = int(last_dict['order_id'])
                new_id = id + 1 
                orders.append({'order_id' : new_id, 'user_id' : data.get('user_id'),'item_ordered' : data.get('item_ordered'), 'item_quantity': data.get('item_quantity')} )
            
            return make_response(jsonify(orders)),201
        # ''' picks data sent from json ,initializes the first order with order_id 1
        #adds whatever was sent from postman to orders, using keys from the data object '''
        #modify method.
        
        
        def modify_order(self,order_id):
             data = request.json
             if data:
                 status = data.get('status')
                 response =  utils.modify_helper(orders,order_id,status)
                 return  make_response(jsonify(response)),201
        #modify_helper is a function in utils.py, it helps us modify the order with the status key and value

             

if __name__ == '__main__': 
    app.run(debug=True)
