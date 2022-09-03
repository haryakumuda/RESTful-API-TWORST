import pandas as pd
import csv
import os
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

names = {"harya": {"age": 23,"gender" : "male"},
         "maurizka":{"age": 23,"gender":"female"}}

videos = {}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument


class HelloName(Resource):
    def get(self, name):
        return names[name]

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    def put(self, video_id):
        return {}



api.add_resource(HelloName, "/<string:name>/")
api.add_resource(Video, "/video/<int:video_id>")



if __name__=="__main__":
    app.run(debug=True)



print("All Done")

'''
test = os.getcwd()

x = pd.read_csv('data.csv', encoding="ISO-8859-1")
print(x)
y = pd.read_csv('new_kamusalay.csv', encoding="ISO-8859-1")
print(y)
z = pd.read_csv('abusive.csv', encoding="ISO-8859-1")
print(z)
dataqu = pd.read_csv('data.csv')
print(dataqu)

'''