import bisect
import itertoolpyts
import operator


class _BNode(object):
	"""pure python b-tree"""
	
	def __init__(self, tree, contents=None, children=None):
		self.tree = tree
		self.contents = contents
		self.children = children
