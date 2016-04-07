 
#!/usr/bin/env python
import csv

fileName = 'baltimore.csv'

try:
	fileName = open(fileName)
except:
	print "The file cannot be opened: ", fileName

csv_reader = csv.reader(fileName)

for row in csv_reader:
	#names = row[12:14]
	firstName = row[14]
	lastname = row[12]
	print  firstName + " " + lastname
