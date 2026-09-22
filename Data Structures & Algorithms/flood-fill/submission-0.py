from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        original_color = image[sr][sc]
        rows,cols = len(image),len(image[0])
        new_image  = image
        def bfs(sr,sc):
            q = deque()
            q.append((sr,sc))
            if new_image[sr][sc] == original_color:
                    new_image[sr][sc] = color

            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            while q:
                r,c = q.popleft()
                #check neighbours left,right,up,down
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and new_image[nr][nc] == original_color:
                        new_image[nr][nc] = color
                        q.append((nr,nc))
            return new_image
        return bfs(sr,sc)



