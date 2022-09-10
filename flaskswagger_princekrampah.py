from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime

#Instantiate flask object
app = Flask(__name__)

#set configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///challenge.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#swagger configs
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "Todo List API"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)


#Instatiate db object
db = SQLAlchemy(app)

#create marshmallow object
ma = Marshmallow(app)