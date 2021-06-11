'''
The min-product of an array is equal to the
minimum value in the array multiplied by the array's sum.

    For example, the array [3,2,5] (minimum value is 2) has 
    a min-product of 2 * (3+2+5) = 2 * 10 = 20.


'''

# finding out the min-product of subarrays of an array
from typing import List
def find_sub_arrays(arr:List)->List:
	ll = []
	for i in range(len(arr)):
		r = i+1
		while r <= len(arr):
			sub = arr[i:r]
			ll.append(sub)
			r = r+1
	return ll



def max_min_product(arr:List)->int:
	sub_arr = find_sub_arrays(arr)
	max_ = 0
	ret = {}
	for j, i in enumerate(sub_arr):
		ret[j] = min(i) * sum(i)
		if ret[j] > max_:
			max_ = ret[j]
			ret_k = i
	return (ret_k, max_)


ls = [3,1,5,6,4,2]
print(max_min_product(ls))