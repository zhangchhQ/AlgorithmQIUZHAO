class Solution:
    def minPathSum(self, grid) -> int:
        if not grid:
            return None
        w = len(grid[0])
        h = len(grid)
        dp = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(0, h):
            for j in range(0, w):
                if i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

sol = Solution()
sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])