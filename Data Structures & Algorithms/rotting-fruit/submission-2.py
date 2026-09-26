from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid), len(grid[0])
        vis=grid
        fresh = 0
        time=0
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c,0))
                if grid[r][c]==1:
                    fresh+=1
        while q:
                
                r,c,time = q.popleft()
                t=time+1
                #check up,down, left, right 
                directions = ((0,1),(0,-1),(1,0),(-1,0))
                for dr, dc in directions:
                    nr , nc = r+dr , c+dc
                    
                    if 0<= nr < rows and 0<=nc<cols and vis[nr][nc]==1:
                        q.append((nr,nc,t))
                        vis[nr][nc] = 2
                        fresh-=1
        if fresh >0:
            return -1
        return time

        


        