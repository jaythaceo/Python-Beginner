class LinkedStack:
	""" LIFO Stack inplementation using a singly linked list for storage"""

	#---------------- nested _Node Class --------------------------
	class _Node():
		"""Lightweight, nonpublic class for sorting s singly linked node"""
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self.element = element
			self.next = next
			
	#------------------ Stack methods ----------------------------
	def __init__(self):
		"""Create an empty stack"""
		self._head = None
		self._size = 0

	def __len__(self):
		"""Return the number of elements in the stack"""
		return self._size

	def is_empty(self):
		"""Return True if the stack is empty"""
		return self._size == 0

	def push(self, e):
		"""Add element e to the top of the stack"""
		self._head