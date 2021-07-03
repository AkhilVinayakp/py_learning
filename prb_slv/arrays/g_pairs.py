'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

'''
import logging
# from os import name
from typing import List
from collections import Counter
from itertools import combinations
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(message)s')

class Solution:
    # @staticmethod
    # def fact(n:int)->int:
    #     if n <= 1:
    #         return 1
    #     else:
    #         return n * fact(n-1)
    @staticmethod
    def nc2(n:int)->int:
        return (n * (n -1 ))//(1*2)
    def g_pair(self, nums:List)->int:
        counts =  [ i for i in Counter(nums).values()]
        logging.debug(counts)
        s = 0
        for i in counts:
            if i > 1:
                s += Solution.nc2(i)
        print(s)
        return 0



if __name__ == "__main__":
    s = Solution()
    s.g_pair([1,2,3,1,1,3])