# https://leetcode.com/problems/3sum/description/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    s.threeSum()

# create a tuple of 3 all possible combination,
# find the tuple that has the sum = 0.
# how we could find out all possible tuple contains 3 values.


def items3_tuple(nums: List[int]):
    from itertools import combinations
    combs = combinations(nums, 3)
    sums = (tuple(sorted(i)) for i in combs if sum(i)==0)
    sums = set(sums)
    print(list(sums))
