from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name':'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return "Hello World"

# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store

# GET /store
@app.route('/store')
def get_stores():
pass

# POST /store/<string: name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
pass

app.run(port=5000)