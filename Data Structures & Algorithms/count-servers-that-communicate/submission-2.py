from collections import deque

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_communicating = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # BFS Traversal
                    q = deque([(i, j)])
                    grid[i][j] = 0
                    cluster_size = 0
                    
                    while q:
                        r, c = q.popleft()
                        cluster_size += 1
                        
                        # Traverse row
                        for col in range(cols):
                            if grid[r][col] == 1:
                                grid[r][col] = 0
                                q.append((r, col))
                                
                        # Traverse column
                        for row in range(rows):
                            if grid[row][c] == 1:
                                grid[row][c] = 0
                                q.append((row, c))
                                
                    if cluster_size > 1:
                        total_communicating += cluster_size
                        
        return total_communicating