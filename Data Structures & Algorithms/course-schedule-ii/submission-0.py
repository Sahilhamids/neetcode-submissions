class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
         #create adj list
        adj = [[] for _ in range(numCourses)]
        inDegree= [0]*numCourses
        q = deque()
        #add to adj
        for v,u in prerequisites:
            adj[u].append(v)
            inDegree[v]+=1
        # topo sort kahn'n Algo
        count=0
        #append all 0 in degree nodes to q
        for i in range(numCourses):
            if inDegree[i]==0:
                q.append(i)
        #bfs
        stack=[]
        while q:
            node= q.popleft()
            stack.append(node)

            for i in adj[node]:
                inDegree[i]-=1
                if inDegree[i]==0:
                    q.append(i)
        return stack if len(stack)==numCourses else []

        