import sys


N = int(raw_input().strip())

for N in xrange(1,6):
	even = N % 2
if N > 0:
	print "This is a even number"
else:
	print "It's odd"