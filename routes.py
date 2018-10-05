from flask import Blueprint 
from database.controllers.controllers1 import methods
from database.controllers.executer import directions
#from app import app
db = Blueprint('db',__name__)# blueprints is a class or flask based applictions that provides a running environment within it without affectin the rest of the items in that class.
direction=directions()


class endpoints:

    #Register a user
    @db.route("/auth/signup", methods= ['POST'])
    def signup(self):
        return direction.handle_register()
        
    #Login a user
    @db.route("/auth/login", methods=['POST'])
    def login(self):
        return direction.handle_sign_in()

    #Place an order for food
    @db.route("/users/orders", methods=['POST'])
    def place_order(self):
        return direction.handle_place_order()

    #Get the order history for a particular user.
    @db.route("/users/orders", methods=['GET'])
    def get_order_history(self):
        return direction.handle_get_order_history()

    #Get all orders Only Admin (caterer) should have access to this route
    @db.route("/orders/", methods=['GET'])
    def get_all_orders(self):
        return direction.handle_get_all_orders()

    #Fetch a specific order Only Admin (caterer) should have access to this route
    @db.route("/orders​/<int:orderId>", methods=['GET'])
    def fetch_specific_order(self,orderId):
        models_obj = methods()
        return models_obj.fetch_specific_order(orderId)

    #Update the status of an order Only Admin (caterer) should haveaccess to this route. The Status
    # of an order could either be New,Processing, Cancelled or Complete.
    @db.route("/orders​/<int:orderId>", methods=['PUT'])
    def update_status(self,orderId):
        models_obj = modles()
        return models_obj.update_order_status(orderId)

    #Get available menu
    @db.route("/menu",methods=['GET'])
    def get_menu(self):
        return controllers1.handle_get_menu()

    #Add a meal option to the Only Admin (caterer) should have access to this route
    @db.route("/menu",methods=['POST'])
    def add_to_menu(self):
        return direction.handle_add_food_item()