# delete elemet in a list

from typing import List
import logging

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')

class Solution:
    def delete_occ(self, nums : List, val : int)-> int:
        ''' takes a list and return the length after deleting elemets '''
        logging.debug(nums, len(nums))
        for i in nums:
            logging.debug(i)
            if i == val:
                logging.debug(f'before deletion {nums}')
                nums.remove(i)
                logging.debug('removed first occurence of {}, remaining list {}'.format(i, nums))
        return len(nums)
    '''
    the first approch has a bug issue .
    '''
    def delete_val(self, nums:List, val: int)-> int:
        '''different approch '''
        i = 0
        n = len(nums)
        while(i<n):
            logging.debug(f"i = {i}")
            if nums[i] == val:
                logging.debug(f"the value found {nums} at {i}")
                # swap with last value and decrease the length
                nums[i] = nums[n-1]
                logging.debug(f"after swapping list is {nums}")
                n -= 1
            else:
                i += 1
        return n

            

# Test
sln = Solution()
l = [0,1,2,2,3,0,4,2]
# print(sln.delete_occ(l, 2))
print('###################')
print(sln.delete_val(l, 2))
