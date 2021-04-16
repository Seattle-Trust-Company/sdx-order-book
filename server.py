#!/usr/bin/env python3

##
# @file  server.py
# @desc  NA
##


### Imports

import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


### Globals

app = Flask(__name__)
os.environ['FLASK_ENV'] = 'development'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


### API Routes

@app.route('/order', methods=['PUT'])
def placeOrder():
  return jsonify({ 'message': 'Hello!' }), 200


### Main Execution

if __name__ == "__main__":
  app.run(debug=True)

