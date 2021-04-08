'''
Dutch national flag problem.
Write a program that takes an array A and an index i rnto A, and rearranges the elements such
that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.
'''
from typing import List
import logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')

class Solution:
    def solve(self, arr: List, i :int) -> List:
        pivot = arr[i]
        logging.debug(f'pivot = {pivot}')
        left, right = 0, len(arr)-1
        for i in range(len(arr)):
            if arr[i] > pivot:
                pass



sln = Solution()
arr = list(map(int, input('enter the elements of the list:').split()))
print(arr)
i = int(input('enter the pivot:'))
srt_arr = sln.solve(arr, i)
    


