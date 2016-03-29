#!/usr/bin/
fileName = raw_input("Enter the file name: ")
try:
	fileName = open(fileName)
except:
	print "The file cannot be opened: ", fileName

count = 0 
for line in fileName:
	count = count + 1
print "Lines is file: ", count



exit() 