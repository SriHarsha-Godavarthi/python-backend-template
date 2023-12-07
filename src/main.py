#import flask for creating backend server
from flask import Flask
#import flask rest api for rest imlimentation
from flask_restful import Api
#import resources(rest api resource) from rest
from resources import hello_world
#import mangodb dependency
from flask_mongoengine import MongoEngine

# create app
app=Flask(__name__)

#configure mangodb for database settings for making connection
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
#get mangodb instance to use with flask
db = MongoEngine()
#connect flask app with mangodb
db.init_app(app)

#create api for resource registration
api=Api(app)
#register the resource /helloworld with the api
api.add_resource(hello_world.HelloWorld,'/helloworld')
# check if file name is main then only start the server
if(__name__=='__main__'):
    app.run(debug=True)