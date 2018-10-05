from flask import Flask, Blueprint
app = Flask(__name__)

from application.users.routes import db
app.register_blueprint(db)

app.config['SECRET_KEY'] ='\xf9\xd7f\x1f\xd5.\xccR\x92\xf1@PX\xf8$\xa4<\xfa\x9c\xbe\xdaP\x84\xa0'