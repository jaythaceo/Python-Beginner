#
#
# Example of calculating with dictionaires

prices = {
  'GOOG': 535.60,
  'AAPL': 126.76,
  'YHOO': 40.40,
  'FB':   82.37,
  'TWTR': 35.94
}

# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print "Min_price: ", min_price
print "Max_price: ", max_price

print "Sorted prices: "
prices_sorted = sorted(zip(prices.values(), prices.keys()))

for price, name in prices_sorted:
  print ("   ", name, price)