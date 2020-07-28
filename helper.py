from datetime import datetime, date, timedelta
from bson import json_util
import json

def bestSupplier(articleID, dateDiff, db):
    supplier = db.articleSupplier.aggregate([
        {
            "$match": {
                "codigoArticulo": articleID,
                "tiempoEntrega": {"$lte": dateDiff},
            },
        },
        {
            "$sort": {"tiempoEntrega": 1, "precioCompra": 1},
        },
        {"$limit": 1},
    ]);

    response = json_util.dumps(supplier)
    json_supplier = json.loads(response)

    return json_supplier[0]


def calculateActualBalance(articleID, db):
    result = db.articles.aggregate([
        {"$match": {"codigo": articleID}},
        {"$unwind": "$disponibilidad"},
        {
            "$group": {
                "_id": {"codigoArticulo": "$codigo", "precioUnidad": '$precioUnidad'},
                "balanceActual": {"$sum": "$disponibilidad.cantidad"},
            },
        },
        {
            "$project": {
                "_id": 0,
                "codigoArticulo": '$_id.codigoArticulo',
                "precioUnidad": '$_id.precioUnidad',
                "balanceActual": '$balanceActual',
            },
        },
    ])
    response = json_util.dumps(result)
    json_article = json.loads(response)

    unitPrice = int(json_article[0]['precioUnidad'])
    actualBalance = int(json_article[0]['balanceActual'])

    return unitPrice, actualBalance


def differenceInDays(nDate):
    d1 = datetime.strptime(nDate, "%Y-%m-%d")
    d2 = datetime.strptime(str(date.today()), "%Y-%m-%d")
    return abs((d2 - d1).days)


def newDateBuilder(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    return (d1 + timedelta(days=d2)).strftime("%Y-%m-%d")

def automaticOrder(data, db):
    date, articles = data.values()
    diff = differenceInDays(date)

    orders = {}
    dailyConsumption = 0
    wantedDateConsumption = 0
    supplier = ''
    helper = 0
    arrHelper = []

    for article in articles.values():

        exitMovements = db.movements.find({'articleID': article['codigo'], 'movementType': 'EXIT' }).count()

        if ( exitMovements > 0 ):
            avgMovements = db.movements.aggregate([
                { '$match': { 'movementType': 'EXIT', 'articleID': 'ART-001' } },
                { '$group': { '_id': '$articleID', 'avgMovement': { '$avg': "$quantity" } } },
                { '$project': {'_id' : 0, 'avgMovement': { '$ceil': '$avgMovement' } } }
            ])

            daily = json_util.dumps(avgMovements)
            daily = daily.replace('[', '')
            daily = daily.replace(']', '')
            dailyConsumption = int(json.loads(daily)['avgMovement'])
        else:
            dailyConsumption = 2

        consumedToDate = dailyConsumption * diff

        unitPrice, actualBalance = calculateActualBalance(article['codigo'], db)

        if ( consumedToDate >= actualBalance ):
            orderedQuantity = int(article['quantity'])
        else:
            orderedQuantity = actualBalance - consumedToDate
         
            if ( orderedQuantity >= int(article['quantity']) ):
                continue
            else:
                orderedQuantity = int(article['quantity']) - orderedQuantity

        supplier = bestSupplier(article['codigo'], diff, db)

        if (not supplier):
            continue
        else:
            newOrderDate = newDateBuilder(date, int(supplier['tiempoEntrega']))

            articleOrder = {
                "articleID": article['codigo'],
                "orderedQuantity": orderedQuantity,
                "buyPrice": orderedQuantity * unitPrice
            }

            order = {
                "supplierID": supplier['codigoSuplidor'],
                "orderDate": newOrderDate,
                "totalAmount": articleOrder['buyPrice'],
                "articles": articleOrder
            }

        orders[helper] = order
        helper = helper + 1

    return orders
    