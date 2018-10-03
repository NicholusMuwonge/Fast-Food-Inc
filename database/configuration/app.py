from flask import Flask
from database1 import Databaseconnection
db=Databaseconnection()
# db.create_tables()
# db.create_userhistory()
# db.create_user
db.adminstrator()

app = Flask(__name__)



if __name__=="__main__":
    app.run(debug=True)

