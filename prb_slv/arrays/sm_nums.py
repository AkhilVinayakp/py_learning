
'''
Given the array nums, for each nums[i] find out how many numbers 
in the array are smaller than it. That is, for each nums[i] you have to 
count the number of valid 
j's such that j != i and nums[j] < nums[i].
'''
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        arr = sorted(nums)
        out.extend([arr.index(i) for i in nums])
        return out
    

if __name__ == "__main___":
    t = [8,1,2,2,3]
    s = Solution()
    print(s.smallerNumbersThanCurrent(t))
