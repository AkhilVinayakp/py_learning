# sliding window problem 
# given a string s and another string t find k minimum windows in s that contains all the characters in t

# pseudocode
"""
l = [] # returned list
for i in range(len(s))
    for j in range(len(t), len(s)):
        let = t.split()
        sl = s[i:j]
        if len(sl) < k:
            continue
        flag = 0
        for l in let:
            if l in sl:
                flag +=1
        if flag = len(let):
            l.append(sl)
            l.sort(sl, key = lambda x : len(x))
            if len(l) == k:
                return l
            break

"""

import logging
from os import kill
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
#
class Solution:
    def __init__(self, s,t,k) -> None:
        self.s = s
        self.t:str = t
        self.k = k
    def solve(self):
        l = [] # returned list
        for i in range(len(self.s)):
            logging.debug(f"i = {i}")
            for j in range(len(self.t)+i, len(self.s)):
                logging.debug(f"j = {j}")
                let = self.t.split()
                sl = self.s[i:j]
                logging.debug(f"t = {self.t} slice = {sl}")
                if len(sl) < len(self.t):
                    continue
                # checking if the letters present in the sl slice
                flag = 0 # keep track count
                for le in let:
                    if le in sl:
                        flag += 1
                if flag == len(let):
                    l.append(sl)
                    l.sort(key= lambda x: len(x))
                    logging.debug(f" appended list = {l}")
                    if len(l) == self.k:
                        # logging.debug(f"retunring l with length{self.k} l = {l}")
                        pass
                        # return l
                    break
        logging.debug(f"l = {l}")
        return l                 

s = 'ABCCEFGABCIOPBCDARMACDFBN'
t = 'ABC'
k = 3
sln = Solution(s,t,k)
print(sln.solve())