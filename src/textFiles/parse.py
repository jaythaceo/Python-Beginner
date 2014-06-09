#!/usr/bin/

f = open('text.txt', 'r')
for line in f:
    if line.startswith('Jason'):
        print line
f.close()
