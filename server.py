from flask import Flask
from flask import render_template, Response, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import json_util
import json
import bson

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/tareaCompras"
mongo = PyMongo(app)
db = mongo.db
articlesDict = {}
articlesDictHelper = {}


@app.route("/")
def index():
    return render_template('dashboard.html')

@app.route('/movements', methods=['POST'])
def insert_movement():

    movementID = db.movements.count() + 1
    warehouseID = request.form.get('warehouseID')
    movementType = request.form.get('movementType')
    articleID = request.form.get('articleID')
    quantity = int(request.form.get('quantity'))
    units = 'x'
    
    db.movements.insert_one(
        {
            "movementID": movementID,
            "warehouseID": warehouseID,
            "movementType": movementType.upper(),
            "articleID": articleID,
            "quantity": quantity,
            "units": units,
        },
    )
    
    article = db.articles.aggregate([
        { "$match": { "codigo": { "$eq": articleID } } },
        { "$unwind": "$disponibilidad" },
        { "$match": { "disponibilidad.codigoAlmacen": { "$eq": warehouseID } } },
        { "$project": {"_id" : 0, "cantidad": "$disponibilidad.cantidad", } }
    ])

    currentQuantity = json_util.dumps(article)
    currentQuantity = currentQuantity.replace('[', '')
    currentQuantity = currentQuantity.replace(']', '')

    current = json.loads(currentQuantity)['cantidad']

    if (movementType.upper() == 'ENTRY'):
        newQuantity = current + quantity
    else:
        newQuantity = current - quantity

    db.articles.update_one(
        {"codigo" : articleID, "disponibilidad.codigoAlmacen" : warehouseID},
        { "$set" : { "disponibilidad.$.cantidad" : newQuantity }}
    )

    return redirect(url_for('get_movements_page'))

@app.route('/movements', methods=['GET'])
def get_movements_page():
    data = db.movements.find().sort('movementID', -1)
    return render_template('movements.html', movements = data)


@app.route('/orders', methods=['GET'])
def get_orders_page():
    select_articles = db.articles.find()
    return render_template('orders.html', articles=articlesDictHelper.items(), select_articles=select_articles)

@app.route('/orders', methods=['POST'])
def get_order():
    date = request.form.get('date')
    return redirect(url_for('get_orders_page'))


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

@app.route('/<warehouseId>/articles', methods=['GET'])
def get_warehouse_articles(warehouseId):

    articles = db.articles.aggregate([
        { "$unwind": "$disponibilidad" },
        { "$match": { "disponibilidad.codigoAlmacen": { "$eq": warehouseId } } },
        { "$project": {"_id" : 0, "codigo": "$codigo", "nombre": "$nombre" } }
    ])
    json_articles = json_util.dumps(articles)
    return Response(json_articles, mimetype="application/json")

if __name__ == "__main__":
    app.run()
