 
#!/usr/bin/env python
import csv
"""
fileName = csv.DictReader(open('baltimore.csv', delimiter= ','))

for i in fileName:
	print(i["FirstName"]),
	print(i["LastName"]),
	print(i["vAddress"]),
	print(i["mCity"])
"""
def csv_parser(fileName):
	reader = csv.DictReader(fileName)
	for line in reader:
		print(line["FirstName"]),
		print(line["LastName"]),
		print(line["vAddress"]),
		print(line["mCity"]),
		print(line["Zip5"])


if __name__ == '__main__':
	with open('baltimore.csv') as fileName:
		csv_parser(fileName)