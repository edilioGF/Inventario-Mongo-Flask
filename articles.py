from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client = MongoClient('localhost')

db = client['tareaCompras']

'''
articlesdb = db['articles']

articles = [
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
    },
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
    },
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
    },
    {
        "codigo": 'ART-004',
        "nombre": 'Cooler premium',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 3},
            {"codigoAlmacen": 'ALM-002', "cantidad": 8},
            {"codigoAlmacen": 'ALM-003', "cantidad": 1},
        ],
        "precioUnidad": 25,
    },
    {
        "codigo": 'ART-005',
        "nombre": 'Motherboard X',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 2},
            {"codigoAlmacen": 'ALM-002', "cantidad": 1},
            {"codigoAlmacen": 'ALM-003', "cantidad": 3},
        ],
        "precioUnidad": 35,
    },
    {
        "codigo": 'ART-006',
        "nombre": 'RAM 8GB',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 12},
            {"codigoAlmacen": 'ALM-002', "cantidad": 21},
            {"codigoAlmacen": 'ALM-003', "cantidad": 13},
        ],
        "precioUnidad": 15,
    },
    {
        "codigo": 'ART-007',
        "nombre": 'RAM 4GB',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 7},
            {"codigoAlmacen": 'ALM-002', "cantidad": 5},
            {"codigoAlmacen": 'ALM-003', "cantidad": 1},
        ],
        "precioUnidad": 10,
    },
    {
        "codigo": 'ART-008',
        "nombre": 'SSD 256GB',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 5},
            {"codigoAlmacen": 'ALM-002', "cantidad": 7},
            {"codigoAlmacen": 'ALM-003', "cantidad": 18},
        ],
        "precioUnidad": 40,
    },
    {
        "codigo": 'ART-009',
        "nombre": 'HDD 1TB',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 1},
            {"codigoAlmacen": 'ALM-002', "cantidad": 4},
            {"codigoAlmacen": 'ALM-003', "cantidad": 9},
        ],
        "precioUnidad": 20,
    },
    {
        "codigo": 'ART-010',
        "nombre": 'Video Card X',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 5},
            {"codigoAlmacen": 'ALM-002', "cantidad": 7},
            {"codigoAlmacen": 'ALM-003', "cantidad": 18},
        ],
        "precioUnidad": 40,
    },
    {
        "codigo": 'ART-011',
        "nombre": 'Video Card A',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 2},
            {"codigoAlmacen": 'ALM-002', "cantidad": 3},
            {"codigoAlmacen": 'ALM-003', "cantidad": 9},
        ],
        "precioUnidad": 40,
    },
    {
        "codigo": 'ART-012',
        "nombre": 'Case X',
        "descripcion": 'Tiene un paquete de luces RGB',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 5},
            {"codigoAlmacen": 'ALM-002', "cantidad": 10},
            {"codigoAlmacen": 'ALM-003', "cantidad": 11},
        ],
        "precioUnidad": 24,
    },
    {
        "codigo": 'ART-013',
        "nombre": 'PSU X',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 1},
            {"codigoAlmacen": 'ALM-002', "cantidad": 2},
            {"codigoAlmacen": 'ALM-003', "cantidad": 3},
        ],
        "precioUnidad": 10,
    },
    {
        "codigo": 'ART-014',
        "nombre": 'Monitor ACER',
        "descripcion": '24in 120hz',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 10},
            {"codigoAlmacen": 'ALM-002', "cantidad": 12},
            {"codigoAlmacen": 'ALM-003', "cantidad": 13},
        ],
        "precioUnidad": 70,
    },
    {
        "codigo": 'ART-015',
        "nombre": 'Samsung Curved',
        "descripcion": '27in',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 1},
            {"codigoAlmacen": 'ALM-002', "cantidad": 2},
            {"codigoAlmacen": 'ALM-003', "cantidad": 3},
        ],
        "precioUnidad": 90,
    },
    {
        "codigo": 'ART-016',
        "nombre": 'Mouse Generico',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 20},
            {"codigoAlmacen": 'ALM-002', "cantidad": 25},
            {"codigoAlmacen": 'ALM-003', "cantidad": 13},
        ],
        "precioUnidad": 5,
    },
    {
        "codigo": 'ART-017',
        "nombre": 'Mouse Ergonomico X',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 12},
            {"codigoAlmacen": 'ALM-002', "cantidad": 27},
            {"codigoAlmacen": 'ALM-003', "cantidad": 3},
        ],
        "precioUnidad": 37,
    },
    {
        "codigo": 'ART-018',
        "nombre": 'Trackpad inalambrico',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 5},
            {"codigoAlmacen": 'ALM-002', "cantidad": 7},
            {"codigoAlmacen": 'ALM-003', "cantidad": 13},
        ],
        "precioUnidad": 40,
    },
    {
        "codigo": 'ART-019',
        "nombre": 'Teclado inalambrico',
        "descripcion": 'Tiene luces RGB y es mecanico',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 12},
            {"codigoAlmacen": 'ALM-002', "cantidad": 22},
            {"codigoAlmacen": 'ALM-003', "cantidad": 32},
        ],
        "precioUnidad": 20,
    },
    {
        "codigo": 'ART-020',
        "nombre": 'Teclado generico X',
        "descripcion": '',
        "disponibilidad": [
            {"codigoAlmacen": 'ALM-001', "cantidad": 2},
            {"codigoAlmacen": 'ALM-002', "cantidad": 17},
            {"codigoAlmacen": 'ALM-003', "cantidad": 13},
        ],
        "precioUnidad": 7,
    },
]

articlesdb.insert_many(articles)
'''

suppliersdb = db['suppliers']

suppliers = [
    {
        "codigo": 'SUP-001',
        "name" : "Distribuidora",
        "address" : "Santiago",
        "phone" : "8095813000"
    },
    {
        "codigo": 'SUP-002',
        "name" : "PiezasYa",
        "address" : "Santo Domingo",
        "phone" : "8095813001"
    },
    {
        "codigo": 'SUP-003',
        "name" : "Prodacom",
        "address" : "Santiago",
        "phone" : "8095813002"
    },
    {
        "codigo": 'SUP-004',
        "name" : "Repuestos",
        "address" : "Puerto Plata",
        "phone" : "8095813003"
    },
    {
        "codigo": 'SUP-005',
        "name" : "Cecomsa",
        "address" : "Santiago",
        "phone" : "8095813004"
    }
]

suppliersdb.insert_many(suppliers)


articleSupplierdb = db['articleSupplier']

articlesSuppliers = [
    {
        "codigoArticulo": 'ART-001',
        "codigoSuplidor" : "SUP-001",
        "tiempoEntrega" : 3,
        "precioCompra" : 100
    },
    {
        "codigoArticulo": 'ART-001',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 5,
        "precioCompra" : 80
    },
    {
        "codigoArticulo": 'ART-002',
        "codigoSuplidor" : "SUP-002",
        "tiempoEntrega" : 4,
        "precioCompra" : 50
    },
    {
        "codigoArticulo": 'ART-002',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 5,
        "precioCompra" : 45
    },
    {
        "codigoArticulo": 'ART-003',
        "codigoSuplidor" : "SUP-002",
        "tiempoEntrega" : 3,
        "precioCompra" : 100
    },
    {
        "codigoArticulo": 'ART-003',
        "codigoSuplidor" : "SUP-005",
        "tiempoEntrega" : 5,
        "precioCompra" : 80
    },
    {
        "codigoArticulo": 'ART-004',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 2,
        "precioCompra" : 60
    },
    {
        "codigoArticulo": 'ART-004',
        "codigoSuplidor" : "SUP-004",
        "tiempoEntrega" : 1,
        "precioCompra" : 80
    },
    {
        "codigoArticulo": 'ART-005',
        "codigoSuplidor" : "SUP-001",
        "tiempoEntrega" : 3,
        "precioCompra" : 100
    },
    {
        "codigoArticulo": 'ART-005',
        "codigoSuplidor" : "SUP-005",
        "tiempoEntrega" : 6,
        "precioCompra" : 80
    },
    {
        "codigoArticulo": 'ART-006',
        "codigoSuplidor" : "SUP-005",
        "tiempoEntrega" : 5,
        "precioCompra" : 50
    },
    {
        "codigoArticulo": 'ART-006',
        "codigoSuplidor" : "SUP-002",
        "tiempoEntrega" : 3,
        "precioCompra" : 70
    },
    {
        "codigoArticulo": 'ART-007',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 3,
        "precioCompra" : 100
    },
    {
        "codigoArticulo": 'ART-007',
        "codigoSuplidor" : "SUP-004",
        "tiempoEntrega" : 2,
        "precioCompra" : 90
    },
    {
        "codigoArticulo": 'ART-008',
        "codigoSuplidor" : "SUP-001",
        "tiempoEntrega" : 5,
        "precioCompra" : 40
    },
    {
        "codigoArticulo": 'ART-008',
        "codigoSuplidor" : "SUP-002",
        "tiempoEntrega" : 2,
        "precioCompra" : 60
    },
    {
        "codigoArticulo": 'ART-009',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 6,
        "precioCompra" : 70
    },
    {
        "codigoArticulo": 'ART-009',
        "codigoSuplidor" : "SUP-004",
        "tiempoEntrega" : 4,
        "precioCompra" : 80
    },
    {
        "codigoArticulo": 'ART-010',
        "codigoSuplidor" : "SUP-005",
        "tiempoEntrega" : 7,
        "precioCompra" : 30
    },
    {
        "codigoArticulo": 'ART-010',
        "codigoSuplidor" : "SUP-001",
        "tiempoEntrega" : 5,
        "precioCompra" : 40
    },
    {
        "codigoArticulo": 'ART-011',
        "codigoSuplidor" : "SUP-002",
        "tiempoEntrega" : 3,
        "precioCompra" : 100
    },
    {
        "codigoArticulo": 'ART-011',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 5,
        "precioCompra" : 80
    },
    {
        "codigoArticulo": 'ART-012',
        "codigoSuplidor" : "SUP-004",
        "tiempoEntrega" : 3,
        "precioCompra" : 45
    },
    {
        "codigoArticulo": 'ART-012',
        "codigoSuplidor" : "SUP-005",
        "tiempoEntrega" : 1,
        "precioCompra" : 60
    },
    {
        "codigoArticulo": 'ART-013',
        "codigoSuplidor" : "SUP-001",
        "tiempoEntrega" : 5,
        "precioCompra" : 120
    },
    {
        "codigoArticulo": 'ART-013',
        "codigoSuplidor" : "SUP-002",
        "tiempoEntrega" : 3,
        "precioCompra" : 135
    },
    {
        "codigoArticulo": 'ART-014',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 2,
        "precioCompra" : 100
    },
    {
        "codigoArticulo": 'ART-014',
        "codigoSuplidor" : "SUP-004",
        "tiempoEntrega" : 3,
        "precioCompra" : 90
    },
    {
        "codigoArticulo": 'ART-015',
        "codigoSuplidor" : "SUP-005",
        "tiempoEntrega" : 4,
        "precioCompra" : 25
    },
    {
        "codigoArticulo": 'ART-015',
        "codigoSuplidor" : "SUP-001",
        "tiempoEntrega" : 2,
        "precioCompra" : 35
    },
    {
        "codigoArticulo": 'ART-016',
        "codigoSuplidor" : "SUP-002",
        "tiempoEntrega" : 10,
        "precioCompra" : 60
    },
    {
        "codigoArticulo": 'ART-016',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 8,
        "precioCompra" : 50
    },
    {
        "codigoArticulo": 'ART-017',
        "codigoSuplidor" : "SUP-004",
        "tiempoEntrega" : 5,
        "precioCompra" : 100
    },
    {
        "codigoArticulo": 'ART-017',
        "codigoSuplidor" : "SUP-005",
        "tiempoEntrega" : 3,
        "precioCompra" : 70
    },
    {
        "codigoArticulo": 'ART-018',
        "codigoSuplidor" : "SUP-001",
        "tiempoEntrega" : 5,
        "precioCompra" : 150
    },
    {
        "codigoArticulo": 'ART-018',
        "codigoSuplidor" : "SUP-002",
        "tiempoEntrega" : 7,
        "precioCompra" : 130
    },
    {
        "codigoArticulo": 'ART-019',
        "codigoSuplidor" : "SUP-003",
        "tiempoEntrega" : 3,
        "precioCompra" : 40
    },
    {
        "codigoArticulo": 'ART-019',
        "codigoSuplidor" : "SUP-004",
        "tiempoEntrega" : 5,
        "precioCompra" : 55
    },
    {
        "codigoArticulo": 'ART-020',
        "codigoSuplidor" : "SUP-005",
        "tiempoEntrega" : 3,
        "precioCompra" : 100
    },
    {
        "codigoArticulo": 'ART-020',
        "codigoSuplidor" : "SUP-001",
        "tiempoEntrega" : 6,
        "precioCompra" : 85
    },
]

articleSupplierdb.insert_many(articlesSuppliers)


db.movements.insertOne(
    {
        "movementID": 1,
        "warehouseID": 'ALM-001',
        "movementType": 'Entry',
        "articleID": 'ART-001',
        "quantity": 5,
        "units": 'x',
    }
)
