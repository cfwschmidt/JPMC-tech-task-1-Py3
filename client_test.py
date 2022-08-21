import unittest
from random import random
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 
      'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 
      'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (
        quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (
          quote['top_bid']['price'] + quote['top_ask']['price']) / 2
          )
        )

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 
      'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 
      'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (
        quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], 
        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
        ))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateSimpleRatio(self):
    price_pairs = zip(
      [1000 * random() + 1 for i in range(100)], [1000 * random() + 1 for i in range(100)]
      )
    """ ---------- Assertions ----------- """ 
    for a, b in price_pairs:
      self.assertEqual(getRatio(a, b), a/b)

  def test_getRatio_zeroDivisor(self):
    prices = [119.2, 120.48, 121.68, 117.87, 121.2, 120.48, 121.68, 117.87]
    prices[-1:] = [1000 * random() for i in range(100)]

    """ ---------- Assertions ----------- """
    for p in prices:
      self.assertIsNone(getRatio(p, 0))



if __name__ == '__main__':
    unittest.main()
