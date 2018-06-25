from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app2 = Flask(__name__)
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app2.secret_key = 'john'
api = Api(app2)

jwt = JWT(app2, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app2)
    app2.run(port=5001, debug=True)

