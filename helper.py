from datetime import datetime, date, timedelta
from bson import json_util
import json

from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

# client = MongoClient('localhost')

# db = client['tareaCompras']

# articleSupplier = db['articleSupplier']
# articles = db['articles']

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
    # print(json_article[0]['precioUnidad'])

    actualBalance = int(json_article[0]['precioUnidad'])
    unitPrice = int(json_article[0]['balanceActual'])

    return unitPrice, actualBalance


def differenceInDays(nDate):
    d1 = datetime.strptime(nDate, "%Y-%m-%d")
    d2 = datetime.strptime(str(date.today()), "%Y-%m-%d")
    return abs((d2 - d1).days)


def newDateBuilder(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    return (d1 + timedelta(days=d2)).strftime("%Y-%m-%d")

def automaticOrder(data, db):
    print("im in?")
    date, articles = data.values()
    diff = differenceInDays(date)
    # dara = {
    #     date: "",
    #     articles: {
    #         {},
    #         {}, 
    #         {},
    #     }
    # }

    orders = {}
    dailyConsumption = 0
    wantedDateConsumption = 0
    supplier = ''
    helper = 0
    arrHelper = []

    for article in articles.values():
        print("inside for")

        dailyConsumption = 2
        wantedDateConsumption = dailyConsumption * diff
        ''' Tener en cuenta el balance actual ^^'''

        unitPrice, actualBalance = calculateActualBalance(article['codigo'], db)

        # print(article)
        orderedQuantity = wantedDateConsumption + int(article['quantity']) - actualBalance

        if (orderedQuantity <= 0):
            return

        supplier = bestSupplier(article['codigo'], diff, db)

        if (not supplier):
            return

        newOrderDate = newDateBuilder(date, int(supplier['tiempoEntrega']))

        '''
    Suspicious code ahead !!!
    '''
        articleOrder = {
            "articleID": article['codigo'],
            "orderedQuantity": orderedQuantity,
            "buyPrice": orderedQuantity * unitPrice
        }
        # arrHelper.append()
        order = {
            "supplierID": supplier['codigoSuplidor'],
            "orderDate": newOrderDate,
            "totalAmount": articleOrder['buyPrice'],
            "articles": articleOrder
        }

        # orders[supplier['codigoSuplidor']] = order
        orders[helper] = order
        helper = helper + 1
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(orders)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    return orders

    # print("Orders")
    # print(json.dumps(orders, indent=4, sort_keys=True))








'''
SUSPICIOUS CODE AHEAD PART 2
'''

data = {
        "date" : "2020-02-10",
        "articles":
        {
            "article1":
            {
                "codigo": 'ART-001',
                "nombre": 'CPU X',
                "descripcion": '',
                "disponibilidad": [
                    {"codigoAlmacen": 'ALM-001', "cantidad": 50},
                    {"codigoAlmacen": 'ALM-002', "cantidad": 40},
                    {"codigoAlmacen": 'ALM-003', "cantidad": 60},
                ],
                "precioUnidad": 50,
                "quantity": 10
            },
            "article2":
            {
                "codigo": 'ART-002',
                "nombre": 'CPU A',
                "descripcion": '',
                "disponibilidad": [
                    {"codigoAlmacen": 'ALM-001', "cantidad": 10},
                    {"codigoAlmacen": 'ALM-002', "cantidad": 5},
                    {"codigoAlmacen": 'ALM-003', "cantidad": 18},
                ],
                "precioUnidad": 76,
                "quantity": 2
            },
            "article3":
            {
                "codigo": 'ART-003',
                "nombre": 'Cooler generico',
                "descripcion": '',
                "disponibilidad": [
                    {"codigoAlmacen": 'ALM-001', "cantidad": 1},
                    {"codigoAlmacen": 'ALM-002', "cantidad": 5},
                    {"codigoAlmacen": 'ALM-003', "cantidad": 8},
                ],
                "precioUnidad": 10,
                "quantity": 5
            }
        }
    }

# automaticOrder(data)

'''

TODO

NEEDS FOR THIS TO WORK: 
    -Check result according to Alfredo's requirements
    -Try to fix orders (it creates 2 orders from the same supplier
        somehow try to get them together on the same order)
    -IDK WHAT ELSE SO FUCK OFF IMMA SLEEP RIGHT NOW ! 

'''
