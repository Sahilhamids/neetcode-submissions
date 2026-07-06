
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop()+stack.pop())
            elif c == '-':
                v1,v2=stack.pop(),stack.pop()
                stack.append(v2-v1)
            elif c == '*':
                stack.append(stack.pop() * stack.pop() )
            elif c == '/':
                v1,v2=stack.pop(),stack.pop()
                stack.append(int(v2/v1))
            else:
                stack.append(int(c))
        return stack[0]



        