class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        currentString=""
        currentNumber=0
        for c in s:
            if c.isdigit():
                currentNumber = currentNumber * 10 + int(c)
            elif c == "[":
                #push the current state  to the stack and reset
                stack.append((currentString,currentNumber))
                currentString = ""
                currentNumber = 0
            elif c == "]":
                #pop the last state and decode the current block
                lastString, num = stack.pop()
                currentString = lastString + (num * currentString)
            else:
                #accumulate the regular characters
                currentString += c
        return currentString