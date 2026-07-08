class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        for c in path.split("/"):

            if c=="..":
                #go to parent directory
                if stack:
                    stack.pop()
            elif c=="." or not c:
                #ignore
                continue  
            else:
                #valid directory name   
                stack.append(c)
        return "/"+"/".join(stack)             

        

        