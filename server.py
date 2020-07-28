from flask import Flask
from flask import render_template, Response, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import json_util
import json
import bson
from helper import automaticOrder


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
        newQuantity = int(current) + int(quantity)
    else:
        newQuantity = int(current) - int(quantity)

    db.articles.update_one(
        {"codigo" : articleID, "disponibilidad.codigoAlmacen" : warehouseID},
        { "$set" : { "disponibilidad.$.cantidad" : newQuantity }}
    )

    return redirect(url_for('get_movements_page'))

@app.route('/movements', methods=['GET'])
def get_movements_page():
    data = db.movements.find().sort('movementID', -1)
    # for mov in data:
    #     print(mov['articleID'])

    return render_template('movements.html', movements = data)


@app.route('/orders', methods=['GET'])
def get_orders_page():
    select_articles = db.articles.find()
    orders = db.orders.find()

    order_helper = json_util.dumps(orders)
    mixOrders = json.loads(order_helper)
 
    separatedOrders = {}

    for order in mixOrders:
        if ( order['supplierID'] not in separatedOrders ):
            separatedOrders[order['supplierID']] = [order]
        else:
            separatedOrders[order['supplierID']].append(order)
    
    print(separatedOrders)

    return render_template('orders.html', articles=articlesDictHelper.items(), select_articles=select_articles, orders=separatedOrders)

@app.route('/orders', methods=['POST'])
def get_order():
    date = request.form.get('date')

    data = {
        "date": date,
        "articles": articlesDict
    }

    orders = automaticOrder(data, db)
    print(json.dumps(orders, indent=4, sort_keys=True))
    articlesDict.clear()
    articlesDictHelper.clear()

    if(orders) :
        for art in orders.values():
            result = db.orders.insert_one(
            {
                "articleID": art['articles']['articleID'],
                "buyPrice": art['articles']['buyPrice'],
                "orderedQuantity": art['articles']['orderedQuantity'],
                "orderDate": art['orderDate'],
                "supplierID": art['supplierID'],
                "totalAmount": art['totalAmount'],
            },
            )

    '''     
    
    TODO

    somehow refresh orders list in orders page

    '''

    return redirect(url_for('get_orders_page'))


@app.route('/newArticle', methods=['POST'])
def add_article():
    articleID = request.form.get('article')
    quantity = request.form.get('quantity')
    date = request.form.get('date')
    article = db.articles.find_one({"codigo": articleID})

    articlesDict[articleID] = article
    articlesDict[articleID]['quantity'] = quantity
 
    articlesDictHelper[articleID] = {'name' : article['nombre'], 'quantity': quantity, 'code': articleID}

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
