class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        vis = [[0 for _ in range(cols)] for _ in range (rows)]
        ans = 0
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            #mark current node visited
            vis[i][j] = 1

            #check adjecent up,down, left, right if land found then call dfs
            for dr,dc in dir:
                nr,nc = i+dr,j+dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and vis[nr][nc]==0:
                    #call dfs
                    dfs(nr,nc)

        # check top and bottom row
        for c in range(cols):
            if grid[0][c]==1 and vis[0][c]==0:
                dfs(0,c)
            if grid[rows-1][c] ==1 and vis[rows-1][c]==0:
                dfs(rows-1,c)
        # check left and right column
        for r in range(rows):
            if grid[r][0]==1 and vis[r][0]==0:
                dfs(r,0)
            if grid[r][cols-1] ==1 and vis[r][cols-1]==0:
                dfs(r,cols-1)
        # count unvisited lands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and  vis[r][c]==0:
                    ans+=1
        return ans


            
        