from flask import Flask, render_template, Response, request
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/tareaCompras"
mongo = PyMongo(app)
db = mongo.db


@app.route("/")
def index():
    return render_template('dashboard.html')


# @app.route('/movements', methods=['GET'])
# def get_movements():

#     movements = db.inventaryMovement.find()
#     response = json_util.dumps(movements)
#     print("response", response)

#     return Response(response, mimetype="application/json")


@app.route('/movements', methods=['POST'])
def insert_movement():

    movementID = request.json['movementID']
    warehouseID = request.json['warehouseID']
    movementType = request.json['movementType']
    articleID = request.json['articleID']
    quantity = request.json['quantity']
    units = request.json['units']

    db.inventaryMovement.insert_one(
        {
            "movementID": movementID,
            "warehouseID": warehouseID,
            "movementType": movementType.upper(),
            "articleID": articleID,
            "quantity": quantity,
            "units": units,
        },
    )
    return Response("Movement created.", mimetype="text/plain")

@app.route('/movements', methods=['GET'])
def get_movements_page():
    return render_template('movements.html')


@app.route('/orders', methods=['GET'])
def get_orders_page():
    return render_template('orders.html')


if __name__ == "__main__":
    app.run()

