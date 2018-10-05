from flask import Blueprint
from .logic_aut import logic
from database.modles import directions
direction= directions


sign_up= Blueprint('sign_up',__name__)


@sign_up.route("/auth/signup", methods= ['POST'])
def signup(self):
    return direction.handle_register()
    
#Login a user
@sign_up.route("/auth/login", methods=['POST'])
def login(self):
    return direction.handle_sign_in()


