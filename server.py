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


@app.route('/movimientos', methods=['GET'])
def get_movements():

    movimientos = db.movimientoInventario.find()
    response = json_util.dumps(movimientos)
    print("response", response)

    return Response(response, mimetype="application/json")


@app.route('/movimientos', methods=['POST'])
def insert_movement():

    codigoMovimiento = request.json['codigoMovimiento']
    codigoAlmacen = request.json['codigoAlmacen']
    tipoMovimiento = request.json['tipoMovimiento']
    codigoArticulo = request.json['codigoArticulo']
    cantidad = request.json['cantidad']
    unidad = request.json['unidad']

    db.movimientoInventario.insert_one(
        {
            "codigoMovimiento": codigoMovimiento,
            "codigoAlmacen": codigoAlmacen,
            "tipoMovimiento": tipoMovimiento.upper(),
            "codigoArticulo": codigoArticulo,
            "cantidad": cantidad,
            "unidad": unidad,
        },
    )
    return Response("Movement created.", mimetype="text/plain")


if __name__ == "__main__":
    app.run()
