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
def sol1(str1, str2):
    ''''''
    if len(str1) != len(str2):
        return False
    s1 = list(str1)
    s2 = list(str2)
    for item in s1:
        if item not in s2:
            return False
        s1.remove(item)
        s2.remove(item)
    return True
# %%
