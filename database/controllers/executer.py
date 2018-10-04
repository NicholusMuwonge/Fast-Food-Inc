import json
from database.controllers import controllers1
from flask import Flask, make_response, jsonify,abort,request
class directions:
        def handle_register(self):
            self.data = request.json
            models_obj = controllers1.methods()
            return models_obj.register_user(self.data.get('user_id'),self.data.get('email_address'), self.data.get('password'),self.data.get('username'))

        def handle_sign_in(self):
            self.data = request.json
            models_obj = controllers1.methods()
            return models_obj.user_login(self.data.get('username'),self.data.get('password'))

        def handle_place_order(self):
            self.data = request.json
            models_obj = controllers1.methods()
            return models_obj.place_order(self.data.get('order_id'),self.data.get('user_id'),self.data.get('item_id'),self.data.get('item_name'),self.data.get('item_quantity'),self.data.get('price'),self.data.get('status'))

        def handle_get_order_history(self):
            self.data = request.json
            models_obj = controllers1.methods(self)
            return models_obj.get_order_history(self.data.get('user_id'))

        def handle_get_all_orders(self):
            self.data = request.json
            models_obj = controllers1.methods()
            return models_obj.get_all_orders()

        def handle_get_menu(self):
            models_obj = controllers1.methods()
            return models_obj.get_menu()

        def handle_add_food_item(self):
            self.data = request.json
            models_obj = controllers1.methods()
            return models_obj.add_food_item_to_menu(data.get('item_id'),data.get('item_name'), data.get('item_price'))



""" The controller pulls data from json and creates a database of methods class, it accesses the methods in the models and puts data as parameters to those functions from json """