# total number of ways we can reach at a length of n
# by taking either step 1 or step 2.

# normal way.

option = [1, 2]
N = 4
sum = 0
# way builder.(when to end it) -> when we see '1'*N 
# counter
ways = []
flag = True
while flag:
    l = 