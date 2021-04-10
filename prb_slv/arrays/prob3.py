'''
Given an array of integers arr and an integer k.
Find the least number of unique integers after removing exactly k elements.
'''
from collections import Counter
from typing import List
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s ')

class Solution:
    def solve(self, nums:List, k: int)-> int :
        c_dict = Counter(nums)
        c_dict = sorted(c_dict.items(), key= lambda x: x[1])
        logging.debug(f'{c_dict}')
        n = len(c_dict)
        s , q = 0, None
        for i in range(n):
            logging.debug(f'i = {i}')
            
            
            s += c_dict[i][1]
            logging.debug(f's = {s}')
            if s >= k:
                break

        return n-i
    
# Testing
sln = Solution()
print(sln.solve([4,3,1,1,3,3,2],3))
print(sln.solve([5,5,4], 1))