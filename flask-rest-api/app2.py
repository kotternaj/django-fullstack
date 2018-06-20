from flask import Flask
from flask_restful import Resource, Api

app2 = Flask(__name__)
api = Api(app2)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404
    
    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201
    
api.add_resource(Item, '/item/<string:name>') # http//localhost:5001/student/Rolf
    
app2.run(port=5001)

