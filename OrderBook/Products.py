#!/usr/bin/env


# @TODO: Place in DB
products = {
  "BTC-USD": {
        "id": "BTC-USD",
        "display_name": "BTC/USD",
        "base_currency": "BTC",
        "quote_currency": "USD",
        "base_increment": "0.00000001",
        "quote_increment": "0.01000000",
        "base_min_size": "0.00100000",
        "base_max_size": "280.00000000",
        "min_market_funds": "5",
        "max_market_funds": "1000000",
        "status": "online",
        "status_message": "",
        "cancel_only": False,
        "limit_only": False,
        "post_only": False,
        "trading_disabled": False
  }
}

def getProducts():
  return products, 200
  
def getProduct(pid):
  try:
    return products[pid]
  except:
    return { 'msg': 'Unable to grab product with specified ID.' }, 404

def getProductBook(pid):
  return { 'To be developed.' }, 404

def getProductTicker(pid):
  return { 'To be developed.' }, 404
