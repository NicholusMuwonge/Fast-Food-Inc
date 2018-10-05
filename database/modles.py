import json
from database.authentication.logic_aut import logic
from database.user.menu_logic import methods
from flask import Flask, make_response, jsonify,abort,request
class directions:
        @classmethod
        def handle_register(self):
            data = request.json
            models_obj = logic()
            return models_obj.register_user(data.get('user_id'),data.get('email_address'), data.get('password'),data.get('username'))
        @classmethod
        def handle_sign_in(self):
            data = request.json
            models_obj = logic()
            return models_obj.user_login(data.get('username'),data.get('password'))
        @classmethod
        def handle_place_order(self):
            data = request.json
            models_obj = methods()
            return models_obj.place_order(data.get('order_id'),data.get('user_id'),data.get('item_id'),data.get('item_name'),data.get('item_quantity'),data.get('price'),data.get('status'))
        @classmethod
        def handle_get_order_history(self):
            data = request.json
            models_obj =methods()
            return models_obj.get_order_history(data.get('user_id'))
        @classmethod
        def handle_get_all_orders(self):
            data = request.json
            models_obj =methods()
            return models_obj.get_all_orders()
        @classmethod
        def handle_get_menu(self):
            models_obj =methods()
            return models_obj.get_menu()
        @classmethod
        def handle_add_food_item(self):
            data = request.json
            models_obj =methods()
            return models_obj.add_food_item_to_menu(data.get('item_id'),data.get('item_name'), data.get('item_price'))



""" The controller pulls data from json and creates a database of methods class, it accesses the methods in the models and puts data as parameters to those functions from json """