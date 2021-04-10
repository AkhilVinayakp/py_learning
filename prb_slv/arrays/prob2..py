# running sum of an array
from typing import List
import logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')

class Solution:
    def solve(self, nums: List)-> List:
        i = 1 # controls the slicing of the array
        n = len(nums) # upto which slicing is done
        l = [] # list that contains the sum of the sliced list
        while(i<=n):
            t = nums[:i]
            logging.debug(f'{t}')
            l.append(sum(t))
            i +=1
        return l
    def solve2(self, nums:List) -> List:
        """ with out using slicing  """
        rnn_sum = 0 # calculate the running sum
        l = [] # list to append the running sum
        for i in nums:
            rnn_sum += i
            l.append(rnn_sum)
            logging.debug(f'{l}')
        return l

# Testing
l = [1,2,3,4,5]
sln = Solution()
t = sln.solve2(l)
print(t)
