from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        left=0
        righr= len(s)-1
        if len(s) % 2 !=0:
            return False
        stack = deque()
        hmap = {")":"(" , "]":"[" , "}":"{", }
        for char in s:

            if char in hmap:
                if stack and hmap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack








        