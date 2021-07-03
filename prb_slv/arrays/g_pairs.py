'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

'''
import logging
from os import name
from typing import List
from collections import Counter
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(message)s')

class Solution:
    def g_pair(self, nums:List)->int:
        temp = Counter(nums)
        print(temp)
        for i in temp.values():
            logging.debug(i)

if __name__ == "__main__":
    s = Solution()
    s.g_pair([1,2,3,1,1,3])