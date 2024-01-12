'''
https://leetcode.com/problems/valid-anagram/


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false



'''
# %%
s = "anagran"
t = "nagaram"

# %%
def sol1(s, t):
    '''Brute force method.'''
    if len(s) != len(t):
        return False
    s1 = list(s)
    s2 = list(t)
    for item in s1:
        if item not in s2:
            return False
        s2.remove(item)
    return True
# %%
