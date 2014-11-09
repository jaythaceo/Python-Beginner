"""
Google Code Jam
Store Credit Solution

jaythaceo@gmail.com
"""

def selectTwoItems(credit, prices):
  priceIndex = {}
  index = 1
  for price in prices:
    if price in priceIndex and credit == price * 2:
      return [priceIndex[price], index]
    if price in priceIndex:
      index = index + 1
      continue
    priceIndex[price] = index
    index = index + 1
  for price in prices:
    if (credit - price) in priceIndex and credit - price != price:
      return [priceIndex[price], priceIndex[credit - price]]

def run(filename):
  f = open(filename)
  firstLine = True
  lineType = 1
  caseNumber = 1

  for line in f.readlines():
    #print line
    if firstLine == True:
      firstLine = False

      # The number of cases
      continue
    if lineType == 1:
      credit = int(line)
      lineType = 2
      continue
    if lineType == 2:
      lineType = 3
      continue
    if lineType == 3:
      prices = map(int, line.split())
      result = selectTwoItems(credit, prices)
      # print result
      print "Case #" + str(caseNumber) + ": " + str(result[0]) + " " + str(result[1])
      lineType = 1
      caseNumber = caseNumber + 1

smallInputFile = "A-small-practice.in.txt"
largeInputFile = "A-large-practice.in.txt"

print "Small File:"
run(smallInputFile)
print "  "
print "Large File:"
run(largeInputFile)


