# Given an array of integers, return True or False if 
# the array has two numbers that add up to a specific target


import logging
logging.basicConfig(level=logging.DEBUG, format = ' %(levelname)s %(asctime)s : %(message)s')
from typing import List

class TwoSum:
	def __init__(self, A: List, target: int)->bool:
		self.target = target
		self.array = A

	def bruteforce(self):
		for i  in range(len(self.array)-1):
			for j in range(i+1, len(self.array)):
				if self.array[i]+self.array[j] == self.target:
					print(self.array[i], self.array[j])
					return True

	def two_pointer(self):
		''' we use two pointers to start pointing the data from either side of the sorted array'''
		i = 0
		j = len(self.array) - 1
		self.array = sorted(self.array)
		while i<j:
			if self.array[i] + self.array[j] == self.target:
				print(self.array[i], self.array[j])
				return True
			elif self.array[i] + self.array[j] < self.target:
				logging.debug(f" incrementing i = {i+1}")
				i += 1
			else :
				logging.debug(f" decrementing j = {j-1}")
				j -= 1


if __name__ == "__main__":
	r = TwoSum([5,3,2,7,1], 10)
	print(r.bruteforce())
	print(r.two_pointer())


