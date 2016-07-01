#!/usr/bin/python

import csv

f = open('baltimore.csv')
csv_f = csv.reader(f)

for row in csv_f:
	print row[12:4]