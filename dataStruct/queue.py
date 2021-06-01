# python file for implimenting and testing queue implimentaion
#
#
#
#
#
#
#
#
#
#
#
import collection
import time

class Queue:
	""" class implementaion of queue using python list
		for easy implementation we insert data at the front and delete it from last

	"""
	def __init__(self):
		self._data = []

	def enqueue(self, item):
		self._data.insert(0, item)

	def dequeue(self):
		try:
			return self._data.pop()
		except Exception as e:
			print(e)
	@property
	def is_empty(self):
		return self._data == []

	# size of the queue
	def size(self):
		return len(self._data)


class Queue_Col:
	def __init__(self):
		self._data = collection.dequeue()
	def enqueue(self, item):
		self._data.append(item)
	def dequeue(self):
		self._data.popleft()
	@property
	def length(self):
		return len(self._data)



	
		