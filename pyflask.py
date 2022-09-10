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
api = Api(app)

@app.route("/") #Untuk user memasukan url http://127.0.0.1:5000/
def home():
    return render_template("home.html", content="dude") #Untuk menuju page html // content adalah variabel di index.html


@app.route("/tweet", methods=["GET","POST"])
def tweet():
    if request.method == "POST":
        tweet = request.form["twt"]
        tweet = preprocess(tweet)
        return redirect(url_for("cleantwt", twt=tweet))
    elif request.method == "GET":
        return render_template("tweet.html")

@app.route("/preprocess/<twt>")
def cleantwt(twt):
    return f"<h1>Cleaned Text</h1><h3>{twt}</h3>"


if __name__=="__main__":
    app.run(debug=True)



print("All Done")