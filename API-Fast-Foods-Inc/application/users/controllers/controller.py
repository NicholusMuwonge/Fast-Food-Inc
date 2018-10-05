import json
from application.users.models import models
from flask import Flask, make_response, jsonify,abort,request

def handle_register():
    data = request.json
    models_obj = models.DatabaseConnection()
    models_obj.register_user(data.get('user_id'),data.get('email_address'), data.get('password'), data.get('username'))
    return 'done'

def handle_sign_in():
    data = request.json
    models_obj = models.DatabaseConnection()
    return models_obj.user_login(data.get('username'),data.get('password'))

def handle_place_order():
    data = request.json
    models_obj = models.DatabaseConnection()
    return models_obj.place_order(data.get('order_id'),data.get('user_id'),data.get('item_id'),data.get('item_name'),data.get('item_quantity'),data.get('price'),data.get('status'))

def handle_get_order_history():
    data = request.json
    models_obj = models.DatabaseConnection()
    return models_obj.get_order_history(data.get('user_id'))

def handle_get_all_orders():
    data = request.json
    models_obj = models.DatabaseConnection()
    return models_obj.qet_all_orders()

def handle_get_menu():
    models_obj = models.DatabaseConnection()  #pick logic from the logic bit and access class database connection
    
    return models_obj.qet_menu()

def handle_add_food_item():
    data = request.json
    models_obj = models.DatabaseConnection()
    return models_obj.add_food_item_to_menu(data.get('item_name'), data.get('item_price'))



