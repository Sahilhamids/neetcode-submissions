class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for c in operations:
            if c == '+' :
                val1=stack[-1]
                val2=stack[-2]   
                stack.append(val1+val2)
            elif c == 'C':
                val = stack.pop()
            elif c == 'D':
                val = stack[-1] * 2
                stack.append(val)
            else:
                stack.append(int(c))
        return sum(stack)

        