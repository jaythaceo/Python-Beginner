#!/usr/bin/env python

try:
	from HTMLParser import HTMLParser
	from urllib2 import urlopen
except ImportError:
	from html.parser import HTMLParser
	from urllib.request import urlopen
import sys

class PrintLinks(HTMLParser):
	"""docstring for PrintLinks"""
	def handle_starttag(self,tag, attrs):
		if tag == 'a':
			for name, value in attrs:
				if name == 'href': print(value)

p = PrintLinks()
u = urlopen(sys.argv[1])
data = u.read()
charset = u.info().getparam('charset')
p.feed(data.decode(charset))
p.close()