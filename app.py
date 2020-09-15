from flask import Flask, jsonify, request
from flask_cors import CORS

from helpers import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Fantasy Team'})

@app.route('/players', methods=['GET','POST'])
def players():
    fns = {
        'GET': index,
        'POST': create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/players/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def player(id):
    fns = {
    'GET': show,
    'PATCH': update,
    'DELETE': destroy
    }
    resp, code = fns[request.method](request, id)
    return jsonify(resp), code

app.run(debug=True)
