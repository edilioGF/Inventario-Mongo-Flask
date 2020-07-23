from flask import Flask
from flask import render_template, Response, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/tareaCompras"
mongo = PyMongo(app)
db = mongo.db
articlesDict = {}
articlesDictHelper = {}


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
    return render_template('orders.html', articles=articlesDictHelper.items())


@app.route('/newArticle', methods=['POST'])
def add_article():
    articleName = request.form.get('article')
    quantity = request.form.get('quantity')
    date = request.form.get('date')
    article = db.articles.find_one({"codigo": articleName})

    for i in range(len(articlesDict)):
        if (i == (len(articlesDict) - 1)):
            articlesDict["article" + str(i + 2)] = article

    if (len(articlesDict) == 0):
        articlesDict["article1"] = article
 

    for article in articlesDict.values():
        articlesDictHelper[articleName] = {'name' : article['nombre'], 'quantity': quantity, 'date': date}

    print(articlesDictHelper)


    return redirect(url_for('get_orders_page'))


if __name__ == "__main__":
    app.run()

