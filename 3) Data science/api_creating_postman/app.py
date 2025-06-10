from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)

api = Api(app)

catalog = [
    {
        'id': 1,
        'name': 'Apple',
        'cost': 1200
    },
    {
        'id': 2,
        'name': 'Banana',
        'cost': 900
    },
    {
        'id': 3,
        'name': 'Orange',
        'cost': 1500
    },
    {
        'id': 4,
        'name': 'Pear',
        'cost': 2000
    },

]

class Catalog(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(catalog), 200

        for ctg in catalog:
            if ctg['id'] == id:
                return ctg, 200
        return "Not found this fruit", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('cost')

        params = parser.parse_args(strict=True)
        for ctg in catalog:
            if id == ctg['id']:
                return f"Fruit with ID = {id} already exists", 400

        fruit = {
            "id": int(id),
            "name": params["name"],
            "cost": params["cost"],
        }

        catalog.append(fruit)

        return fruit, 201


    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('cost')

        params = parser.parse_args(strict=True)
        for ctg in catalog:
            if id == ctg['id']:
                ctg['name'] = params['name']
                ctg['cost'] = params['cost']
                return ctg, 201
            fruit = {
                "id": int(id),
                "name": params["name"],
                "cost": params["cost"],
            }
        catalog.append(fruit)

        return fruit, 201

    def delete(self, id):
        global catalog
        not_found = True
        for ctg in catalog:
            if ctg['id'] == id:
                not_found = False
        if not_found:
            return f"Not found this ID = {id}", 404

        catalog = [ctg for ctg in catalog if ctg["id"] != id]
        return f"Phone with ID = {id} is deleted", 200


api.add_resource(Catalog, "/catalog", "/catalog/", "/catalog/<int:id>")
app.run(debug=True)
