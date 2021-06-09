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
import collections
# import time

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

	def show_queue(self):
		for i in self._data:
			print(i, end = '\t')


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
	def show_queue(self):
		for i in self._data:
			print(i, end = '\t')



	
		
# testing 
if __name__ == "__main___":
	print("hha")
	q = Queue()
	q.enqueue(12)
	q.enqueue(34)
	q.enqueue(64)
	q.show_queue()
	q.dequeue()
	q.dequeue()

	print("using queue implimented using collection.dequeue")
	e = Queue_Col()
	e.enqueue(32)
	e.enqueue(324)
	e.show_queue()
