# ADT for queue
import collections
import logging

class Queue:
	""" Implimentaion of queue using collection.dequeue
	fields:
	_data : collection.deque

	methods:
	---------
	enqueue:
	dequeue:
	show:

	properties:
	-----------
	is_empty:
	length:


	"""
	def __init__(self, logging = True):
		self._data = collections.deque()

	def enqueue(self, item):
		self._data.append(item)

	def dequeue(self):
		try:
			self._data.popleft()
		except Expection as e:
			print(e)
	def show(self):
		for i in self._data:
			print(i, end = '\t')
		else:
			print()

	@property
	def is_empty(self):
		return len(self._data) <= 0

	@property
	def length(self):
		return len(self._data)


if __name__ == '__main__':
	q = Queue()
	q.enqueue(21)
	q.enqueue(2323)
	q.show()
	q.dequeue()
	q.show()
