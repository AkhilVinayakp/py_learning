# intersection of two sorted list in python
# using two pointers: one for eact array


from typing import List
def intersection(l1:List, l2:List)->List:
	# creating pointer for both
	p = 0
	q = 0
	# list that retain intersections
	inter:List = []
	while(p<len(l1) and q < len(l2)):
		if l1[p] == l2[q]:
			inter.append(l1[p])
			q += 1
			p += 1
		elif l1[p] < l2[q]:
			p += 1
		else:
			q += 1
	inter = set(inter)
	return inter


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]
print(*intersection(A, B))
