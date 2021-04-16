#!/usr/bin/env python3

class MatchingEngine:

  # Indexes
  stocks = {
    "SDX": {
      'name': 'Seattle Digital Exchange',
      'acronym': 'SDX',
      'address': '0x220302023fn49d2ecc2cev3'
    },
    "TSLA": 1
  }

  def __init__(self):
    self.books = []
    for name, info in stocks:
      book = Book(name, info)
      books.append(book)

  def currentPrice(self, target, source):
    '''
    @desc   gets price of target in terms of source currency
    --
    @param  target
    @param  source
    '''
    return None

