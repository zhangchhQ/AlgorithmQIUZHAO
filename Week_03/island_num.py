class Solution:
    def numIslands(self, grid):
        island_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island_num += 1
                    self.destory_land(grid, i, j)
        return island_num

    def destory_land(self, grid, i, j):
        # terminator
        w = len(grid[0])
        h = len(grid)
        if i >= h or j >= w or grid[i][j] != '1' or j < 0 or i < 0:
            return
        # process
        grid[i][j] = '0'
        self.destory_land(grid, i+1, j)
        self.destory_land(grid, i, j+1)
        self.destory_land(grid, i - 1, j)
        self.destory_land(grid, i, j - 1)

sol = Solution()
ret = sol.numIslands([["1","0","1","1","0","1","1"]])
print(ret)