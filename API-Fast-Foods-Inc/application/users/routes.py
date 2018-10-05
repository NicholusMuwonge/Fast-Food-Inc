from flask import Blueprint,request 
import json 
from application.users.models import models
from application.users.controllers import controller
db = Blueprint('db',__name__)
 
#Register a user
@db.route("/v1/auth/signup", methods= ['POST'])
def signup():
    return controller.handle_register()
     
#Login a user
@db.route("/v1/auth/login", methods=['POST'])
def login():
    return controller.handle_sign_in()

#Place an order for food
@db.route("/v1/users/orders", methods=['POST'])
def place_order():
    return controller.handle_place_order()

#Get the order history for a particular user.
@db.route("/v1/users/orders", methods=['GET'])
def get_order_history():
    return controller.handle_get_order_history()

#Get all orders Only Admin (caterer) should have access to this route
@db.route("/v1/orders/", methods=['GET'])
def get_all_orders():
    return controller.handle_get_all_orders()

#Fetch a specific order Only Admin (caterer) should have access to this route
@db.route("/v1/orders​/<int:orderId>", methods=['GET'])
def fetch_specific_order(orderId):
    models_obj = models.DatabaseConnection()
    return models_obj.fetch_specific_order(orderId)

#Update the status of an order Only Admin (caterer) should haveaccess to this route. The Status
# of an order could either be New,Processing, Cancelled or Complete.
@db.route("/v1/orders​/<int:orderId>", methods=['PUT'])
def update_status(orderId):
    models_obj = models.DatabaseConnection()
    return models_obj.update_order_status(orderId)

#Get available menu
@db.route("/v1/menu",methods=['GET'])
def get_menu():
    return controller.handle_get_menu()

#Add a meal option to the Only Admin (caterer) should have access to this route
@db.route("/v1/menu",methods=['POST'])
def add_to_menu():
    return controller.handle_add_food_item()