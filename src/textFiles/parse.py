#!/usr/bin/
fileName = raw_input("Enter the file name: ")
try:
	fileName = open(fileName)
except:
	print "The file cannot be opened: ", fileName
	exit()

