"""A Python Flask REST API BoilerPlate (CRUD) Style"""

import argparse
from flask import Flask, jsonify, make_response, send_from_directory
from flask_cors import CORS
from routes import request_api
import os
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes import request_api

from flask import Flask, request, redirect, url_for, render_template, jsonify, make_response, send_from_directory
from flask_cors import CORS
import os
from flask_restful import Api, Resource, reqparse
from datacleaning import preprocess
from apispec import APISpec
import flask_swagger_ui
from flask_swagger_ui import get_swaggerui_blueprint
import argparse


app = Flask(__name__)
APP = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'             #URL untuk buka swagger pertama
API_URL = '/static/swagger.json'       #URL untuk UI swagger.json

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL, 
    config={
        'app_name': "Binar Gold Challenge"
    }
)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###




### Ini apa belum tau ###
APP.register_blueprint(request_api.get_blueprint())

@APP.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@APP.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)

@APP.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@APP.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)
### end dari ketidaktahuan ###






### Untuk Run Flask APInya ###
if __name__ == '__main__':

    
    PARSER = argparse.ArgumentParser(
        description="Seans-Python-Flask-REST-Boilerplate")
   
    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Running in debug mode")

        CORS = CORS(APP)
        APP.run(host='0.0.0.0', port=PORT, debug=True)
    else:

        APP.run(host='0.0.0.0', port=PORT, debug=True)