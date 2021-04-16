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
from OrderBook import Currencies


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

@app.route('/products/<pid>', methods=['GET'])
def getProduct(pid):
  product, code = Products.getProduct(pid)
  return jsonify(product), code

@app.route('/products/<pid>/book', methods=['GET'])
def getProductBook(pid):
  book, code = Products.getProductBook(pid)
  return jsonify(book), code

@app.route('/products/<pid>/ticker', methods=['GET'])
def getProductTicker(pid):
  tick, code = Products.getProductTicker(pid)
  return jsonify(tick), code

@app.route('/products/<pid>/trades', methods=['GET'])
def getProductTrades(pid):
  trades, code = Products.getProductTrades(pid)
  return jsonify(trades), code

@app.route('/products/<pid>/candles', methods=['GET'])
def getProductCandles(pid):
  candles, code = Products.getProductCandles(pid)
  return jsonify(candles), code

@app.route('/products/<pid>/stats', methods=['GET'])
def getProductStats(pid):
  stats, code = Products.getProductStats(pid)
  return jsonify(stats), code

@app.route('/currencies', methods=['GET'])
def getProducts():
  currencies, code = Currencies.getCurrencies()
  return jsonify(currencies), code

### Main Execution

if __name__ == "__main__":
  app.run(debug=True)

