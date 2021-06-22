# Given an array of numbers consisting of daily stock prices,
# calculate the maximum amount of profit that can be made from 
# buying on one day and selling on another.

from typing import List

st_price = [310, 315, 275, 295, 260, 270,290,230,255,250]
profit:List = []

for i in range(len(st_price)-1):
	for j in range(i+1, len(st_price)):
		if st_price[j] > st_price[i]:
			profit.append(st_price[j] - st_price[i])
		else:
			continue

print(profit, max(profit))