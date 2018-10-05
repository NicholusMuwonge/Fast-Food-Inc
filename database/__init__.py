from flask import Flask,Blueprint
from database.user.menu_routes import endpoints 
from database.authentication.route_auth import sign_up 
from database.user.menu_routes import db

from database.tables.database import Databaseconnection


#from database.controllers.controllers1 import methods

d=Databaseconnection()
d.create_tables()
d.create_userhistory()
d.create_user
d.adminstrator()

app = Flask(__name__)
app.register_blueprint(sign_up)
app.register_blueprint(db)
app.register_blueprint(db,url_prefix="/")
app.register_blueprint(db,url_prefix="/")
app.register_blueprint(db,url_prefix="/")
app.register_blueprint(db,url_prefix="/")





if __name__=="__main__":
    
    

    app.run(debug=True)

