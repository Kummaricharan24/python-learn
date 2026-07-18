from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                if cr < 0 or cr >= rows or cc < 0 or cc >= cols or grid[cr][cc] != "1":
                    continue
                grid[cr][cc] = "0"
                stack.append((cr + 1, cc))
                stack.append((cr - 1, cc))
                stack.append((cr, cc + 1))
                stack.append((cr, cc - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands