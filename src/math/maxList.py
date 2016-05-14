#!/usr/bin/python
"""
Find max value in 
a list
"""
def find_max(n):
	biggest = n[0]
	for val in n:
		if val > biggest:
			biggest = val
	return biggest

