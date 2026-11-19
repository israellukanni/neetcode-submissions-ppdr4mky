class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        memo = {}
        def dfs(r,c):

            if 0 > r  or r >= rows or 0 > c or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            up = dfs(r+1,c)
            down =  dfs(r-1,c)
            left = dfs(r,c-1)
            right = dfs(r,c+1)
            memo[(r,c)] = 1 + up + down + left + right
            return memo[(r,c)]

        
        ma = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ma = max(ma,dfs(r,c))
        return ma
        
