#!/usr/bin/env python

f = open('text.txt', 'r')
watch = f.read()
for line in watch:
  if line.startswith('5'):
   print line

f.close()
