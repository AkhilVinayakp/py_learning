import logging
from typing import List
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s : %(message)s')


class Solution:
    def __init__(self, array:List, mid :int) -> None:
        self.nums = array
        self.mid = mid
    
    def shuffle(self)-> List:
        temp =  [i for i in zip(self.nums[:self.mid], self.nums[self.mid:])]
        l = []
        for i in temp:
            for j in i:
                l.append(j)
        return l

if __name__ == "__main__":
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    print(Solution(nums, n).shuffle())