# 
# Arbitary position increment using arrays
# 
a = [1,3,9] # ans = [1, 4, 0]

def solve(a):
	a = reversed(a)
	a[0] = a[0] + 1
	for i in a:
		t = i + 1