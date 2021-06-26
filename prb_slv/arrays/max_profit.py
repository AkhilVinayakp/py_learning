# Given an array of numbers consisting of daily stock prices,
# calculate the maximum amount of profit that can be made from 
# buying on one day and selling on another.

from typing import List
import logging 
# logging.basicConfig(level=logging.DEBUG, forma

st_price = [310, 315, 275, 295, 260, 270,290,230,255,250]


class MaxProfit:
	def __init__(self, price_list: List) -> None:
		self.stock = price_list
	@property
	def length(self)->int:
		return len(self.stock)

	# method 1 bruteforce method
	def brute_force(self):
		profit:List = []
		for i in range(self.length-1):
			for j in range(i+1, self.length):
				if self.stock[j] > self.stock[i]:
					profit.append(self.stock[j]-self.stock[i])
		return (profit)

	def min_keep(self):
		profit_list = []
		min_ = self.stock[0]
		for i in range(1,self.length):
			profit_list.append(self.stock[i]-min_ if self.stock[i]> min_ else 0)
			if self.stock[i] < min_:
				min_ = self.stock[i]
		return profit_list


t = MaxProfit(st_price)
print(t.brute_force())
print(t.min_keep())