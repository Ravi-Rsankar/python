import pymongo
from pymongo import MongoClient
import datetime
import flask
from flask import jsonify, request, escape, Flask

app = Flask(__name__)

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['pydb']

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/customer', methods=['POST'])
def insert():
    if flask.request.method == 'POST':
        print(request.json)
        post = {"name": request.json['name']}
        customer = db.customer
        cust_id = customer.insert_one(post).inserted_id
        print(cust_id)

    return "", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port=5000)