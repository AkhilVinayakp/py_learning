# deque implimentation in python
# 
# 
# 
from typing import List



class Deque:
	"""
	instance methods:
	1. add_front		=> append_left()
	2. add_rear			=> append()
	3. remove_rear		=> pop()
	4. remove_front		=> popleft()



	"""
	def __init__(self):
		self.deque:List = [] # creates an empty list

	def append_left(self, item: int)->None:
		'''
		add element at the front of the deque
		'''
		self.deque.insert(0, item)

	def append(self, item:int)->None:
		self.deque.append(item)

	def pop(self)->any:
		
		try:
			return self.deque.pop()
		except Exception as e:
			return e

	def popleft(self)-> any:
		''' return the value from the left of the list '''
		try:
			return self.deque.pop(0)
		except Exception as e:
			raise e
	@property
	def is_empty(self):
		return self.deque == []

	@property
	def length(self)->int:
		return len(self.deque)

	#showing the  list
	def print_list(self)->str:
		return " ".join(str(i) for i in self.deque)



if __name__ == '__main__':
	d = Deque()
	d.append(324)
	d.append(2)
	d.append(32)
	print(d.print_list())
	d.append_left(90)
	print(d.print_list())
	print(f"poping from the end {d.pop()} now List is {d.print_list()}")
	print(f" poping from the front of the list {d.popleft()} the list is {d.print_list()}")

