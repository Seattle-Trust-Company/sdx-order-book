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
from OrderBook import Products


### Globals

app = Flask(__name__)
os.environ['FLASK_ENV'] = 'development'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


### API Routes

@app.route('/products', methods=['GET'])
def getProducts():
  products, code = Products.getProducts()
  return jsonify(products), code

@app.route('/product/<pid>', methods=['GET'])
def getProduct(pid):
  product, code = Products.getProduct(pid)
  return jsonify(product), code

@app.route('/product/<pid>/book', methods=['GET'])
def getProductBook(pid):
  book, code = Products.getProductBook(pid)
  return jsonify(book), code

@app.route('/product/<pid>/ticker', methods=['GET'])
def getProductTicker(pid):
  tick, code = Products.getProductTicker(pid)
  return jsonify(tick), code




### Main Execution

if __name__ == "__main__":
  app.run(debug=True)

