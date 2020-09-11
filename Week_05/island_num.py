class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        isnum = 0
        w = len(grid[0])
        h = len(grid)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    isnum += 1
                    self.destory(i, j, h, w, grid)
        return isnum
    def destory(self, i, j, h, w, grid):
        # terminator
        if i >= h or j >= w or grid[i][j]!="1" or j<0 or i < 0:
            return
        # process on
        grid[i][j] = "0"
        self.destory(i,j+1, h, w, grid)
        self.destory(i+1, j, h, w, grid)
        self.destory(i-1, j, h, w, grid)
        self.destory(i, j-1, h, w, grid)