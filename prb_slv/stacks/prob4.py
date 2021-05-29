"""
Given a list of daily temperatures temperatures, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures temperatures = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. 
Each temperature will be an integer in the range [30, 100].

"""

"""
Sudo code
iterate through the list:

"""
from stack_adt import *
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

def solve(temperature):
	dist = []
	for i, j in enumerate(temperature):
		for k in range(i+1, len(temperature)):
			if temperature[k] > j:
				dist.append(k-i)
				break
	if(len(dist) != len(temperature)):
		# print(2)
		for _ in range(len(temperature)-len(dist)):
			dist.append(0)
	print(dist)

solve([73, 74, 75, 71, 69, 72, 76, 73])
