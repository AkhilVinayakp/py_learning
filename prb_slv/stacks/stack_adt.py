# stack adt
"""
 Principle LIFO
 1. push(item)
 2.pop
 3.peek() same as pop but does not delete the fist element
 4. Traverse() Traversal of stack
 5.length
 6 is_empty
"""
from typing import List

class Overflow(Exception):
	pass


class Underflow(Exception):
	pass



class Stack:
	"""
	stack adt :
	field:
	items: List - contains the elements
	limit: int - contains the maximum elements


	"""
	def __init__(self, limit:int = 10):
		self.items:List = []
		self.limit:int = limit

	@property
	def is_empty(self):
		return len(self.items) <= 0
	@property
	def length(self):
		return len(self.items)
	def push(self, item):
		if self.length >= self.limit:
			raise Overflow
		self.items.append(item)

	def pop(self):
		if self.length <= 0:
			raise Underflow
		return self.items.pop()

	def peek(self):
		return self.items[self.length-1]

	def traverse(self):
		for i in reversed(self.items):
			print(i)



if __name__ == "__main__":
	t = Stack(limit = 2)
	t.push(19)
	t.push(12)
	t.push(320)
	t.traverse()
	print(t.peek())
