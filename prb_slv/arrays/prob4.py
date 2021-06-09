

from typing import List
def solve(A:List)->List:
	result:List = []
	srt_list = sorted(A)
	# print(srt_list_asc, srt_list_desc)
	for i in A:
		print(i)
		min_i = 0
		max_i = 0
		# finding the immediate minimum
		i_item = srt_list.index(i)
		print(f"{i} index at sorted {srt_list} is {i_item}")
		if i_item == 0:
			min_i = 0
		else:
			min_i = srt_list[i_item-1]
		if i_item == len(A)-1:
			max_i = 0
		else:
			max_i = srt_list[i_item+1]
		result.append(min_i + max_i)
	return result


A = [1, 9, 0, 6, 3]
print(A)
print(solve(A))