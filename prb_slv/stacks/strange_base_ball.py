# https://leetcode.com/problems/baseball-game/description/

from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for item in operations:
            match item:
                case '+':
                    if len(stack) >= 2:
                        stack.append(stack[-1]+ stack[-2])
                    # check with other cases.
                case 'D':
                    if stack:
                        stack.append(2*stack[-1])
                case 'C':
                    stack.pop()
                case _ :
                    stack.append(int(item))
        return sum(stack)
