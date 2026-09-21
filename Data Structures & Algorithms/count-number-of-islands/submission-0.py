from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        vis = [[0 for _ in range(cols)] for _ in range(rows)]
        q = deque();
        q.append([0,0])
        count=0
        def bfs(r, c):
            q = deque([(r, c)])
            vis[r][c] = 1
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "1" and vis[nr][nc] == 0:
                            vis[nr][nc] = 1
                            q.append((nr, nc))
        for i in range(rows):
            for j in range(cols):
                if vis[i][j] == 0  and grid[i][j]=="1":
                    bfs(i,j)
                    count+=1
        
        return count

                

                
