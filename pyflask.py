from flask import Flask, request, redirect, url_for, render_template
from flask_restful import Api, Resource, reqparse



app = Flask(__name__)
api = Api(app)

@app.route("/") #Untuk user memasukan url http://127.0.0.1:5000/
def home():
    return render_template("home.html", content="dude") #Untuk menuju page html // content adalah variabel di index.html


@app.route("/tweet", methods=["GET","POST"])
def tweet():
    return render_template("tweet.html")






if __name__=="__main__":
    app.run(debug=True)



print("All Done")