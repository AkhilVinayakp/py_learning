# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# algorithms
'''
bruteforce
 for i in range(len(string)-1):
     for j in range(i+1,len(string)):
         y = string[i:j]
         if len(y)%2 == 0 :
             t = Counter(y)
             if t['R'] == t['L']:
                 count ++

'''
from collections import Counter
class Solution:
    def balence(self, s:str)->int:
        count = 0
        l = []
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                # creating substrings iteratively
                y = s[i:j]
                if len(y)%2 ==0:
                    t = Counter(y)
                    if t['R'] == t['L']:
                        count += 1
                        l.append(y)
        return set(l), len(l)


if __name__ == "__main__":
    s = Solution()
    print(s.balence("LLLLRRRR"))