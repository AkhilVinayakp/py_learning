# https://leetcode.com/problems/valid-parentheses/description/


#%%
# sample input
sample1 = "()[]{}"
sorted(sample1)

# we can do with stack
# with out stack how can we do it.
input_pattern = sample1
assert len(input_pattern)%2 != 0, "not a valid pattern"
input_pattern = sorted(input_pattern)
for i in range(0,len(input_pattern)-1, 2):
    if input_pattern[i] != input_pattern[i+1]:
        print("not a valid pattern")
print("valid pattern")


#%%
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        match_pattern = {
            '{' : '}',
            '(' : ')',
            '[' : "]"
        }
        s = sorted(s)
        for i in range(0, len(s)-1, 2):
            pair_match = match_pattern.get(s[i])
            if pair_match != s[i+1]:
                return False
        return True

# %%

# %%
s = Solution()
# %%

# %%
test1 = "()[]{}"
s.isValid(test1)
# %%
test2="([)]"
s.isValid(test2) # fails
# %%
# what went wrong about the first soln
# do not consider the order.
# For the above problem. order matters. It is just not about whether there exist
# a closing bracket for an opening bracket. if it was, the solution may work 
# but not in this case. When looking into patterns, ensure that the order matters or not.

# %%
# with stack. 

# sample stack test
l = [1, 2, 3]
l.append(4)  # add at the end. 
l.pop()  # removes from the end.
# we get LIFO
# %%
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        match_pattern = {
            '{' : '}',
            '(' : ')',
            '[' : "]"
        }
        stack = []
        for item in s:
            if item in match_pattern.keys():
                stack.append(item)
            elif stack and item in match_pattern.values():
                if item != match_pattern[stack.pop()]:
                    return False
            else:
                return False
        return not len(stack)
    
# %%

# %%
s ="))"
prbsln = Solution()
prbsln.isValid(s)
# %%
