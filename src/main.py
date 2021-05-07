import pymongo
# Import the Flask module that has been installed.
from flask import Flask, jsonify, request
from bson.json_util import dumps, loads
import random
import json

# https://www.w3schools.com/python/python_mongodb_getstarted.asp

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase-webservices"]
mycol = mydb["games"]

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"
    
# Annotation that allows the function to be hit at the specific URL. Indicates a GET HTTP method.
@app.route("/bordgames/v1.0/games", methods=["GET"])
# Function that will run when the endpoint is hit.

# curl http://localhost:5000/bordgames/v1.0/games

def get_games():
    # Returns a JSON of the games defined above. jsonify is a Flask function that serializes the object for us.
    lst = list(mycol.find({})) # Converts object to list
    return dumps(lst) # Converts to String
    
# Annotation that allows the function to be hit at the specific URL with a parameter. Indicates a GET HTTP method.
@app.route("/bordgames/v1.0/games/<int:game_id>", methods=["GET"])
# This function requires a parameter from the URL.

# curl http://localhost:5000/bordgames/v1.0/games/0

def get_game(game_id):
    
    myquery = { "id": game_id }
  
    l = list(mycol.find(myquery, {"_id": 0})) # Converts object to list

    return dumps(l) # Converts to String
    
@app.route("/bordgames/v1.0/games/<int:game_id>", methods=["DELETE"])
# This function requires a parameter from the URL.

# curl -X DELETE http://localhost:5000/bordgames/v1.0/games/0

def delete_game(game_id):

    myquery = { "id": game_id }

    mycol.delete_one(myquery)
    
    return "Efface"
    
@app.route("/bordgames/v1.0/games/<int:game_id>", methods=["PUT"])
# This function requires a parameter from the URL.

# curl -X PUT http://localhost:5000/bordgames/v1.0/games/1 

def update_game(game_id):

    myquery = { "id": game_id }
    newvalues = { "$set": { "id": random.randint(0,11) } }

    mycol.update_one(myquery, newvalues)
    
    return "Efface"
    
@app.route("/bordgames/v1.0/games", methods=["POST"])
# This function requires a parameter from the URL.
# $ curl -X POST -H "Content-Type: application/json" -d @json_create_game.txt http://localhost:5000/bordgames/v1.0/games
def add_game():
    x = mycol.insert_one(request.json)
    return "Add"

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()