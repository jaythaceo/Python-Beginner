#!/usr/bin/env python
#Created by Jaythaceo@gmail.com/ google.com/+ceobrooks
# July 17 2014

smallest = -1
print 'Before',smallest
for value in [3,5,34,35]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest = value
	print smallest,value

print 'After', smallest




