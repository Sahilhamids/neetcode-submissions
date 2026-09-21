from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(start_r, start_c):
            q = deque([(start_r, start_c)])
            visited.add((start_r, start_c))
            perimeter = 0

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # 1. Edge of grid or Water -> adds 1 to perimeter
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                        perimeter += 1
                    # 2. Unvisited Land -> visit & add to queue
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return perimeter

        # Find the single island's starting cell and launch BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)

        return 0
        