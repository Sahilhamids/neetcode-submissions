from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])

        max_area = 0
        visited = grid
        def bfs(sr,sc):
            q=deque()
            q.append((sr,sc))
            visited[sr][sc]=0

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            area = 1
            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0<=nr<rows and 0<=nc<cols and visited[nr][nc] and grid[nr][nc]==1:
                        visited[nr][nc] = 0
                        q.append((nr,nc))
                        area+=1
            return area
                    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j]:
                    area = bfs(i,j)
                    max_area = max(max_area, area)
        return max_area
