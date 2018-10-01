from flask import Blueprint  

from application.api.models import models
mod = Blueprint('api',__name__)
 
#index route
@mod.route('/api/v1/')
def index():
    return 'App factory - Fast Foods Inc.'

#our route for getting all orders
@mod.route("/api/v1/orders", methods= ['GET'])
def get_all_orders():
    return models.models.get_all_orders() 

#our route for getting anly one order
@mod.route("/api/v1/orders/<int:order_id>", methods= ['GET'])
def fetch_one_order():
    return models.models.fetch_one_order()

#our route for placing an order
@mod.route("/api/v1/orders", methods= ['POST'])
def place_order():
    return models.models.place_order()

# route for modifying order
@mod.route("/api/v1/orders/<int:order_id>", methods= ['PUT'])
def modify_order():
    return models.models.modify_order()