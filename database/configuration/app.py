from flask import Flask
from database1 import Databaseconnection
db=Databaseconnection()
# db.create_tables()
db.create_user
app = Flask(__name__)



if __name__=="__main__":
    app.run(debug=True)

