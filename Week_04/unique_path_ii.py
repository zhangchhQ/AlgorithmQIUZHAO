class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # 地图中有0，1；要建新的地图存储模版
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        # 边界条件
        # 就一个格子
        if obstacleGrid[0][0] == 1:
            return 0
        # start是障碍物；一行或一列
        # if obstacleGrid[0][0] == 1 or row == 1 or col == 1:
        #     return 1
        dp = [[0 for c in range(col)] for r in range(row)]
        # for r in range(row):
        #     if obstacleGrid[r][0] != 1:
        #         dp[r][0] = 1
        # for c in range(col):
        #     if obstacleGrid[0][c] != 1:
        #         dp[0][c] = 1
        # 全遍历
        for r in range(row):
            for c in range(col):
                # 判断是不是障碍物
                if obstacleGrid[r][c] == 0:
                    # 不是障碍物
                    # 判断在不在边界
                    if r == 0 or c == 0:
                        # 在边界
                        dp[r][c] = 1
                    else:
                        dp[r][c] = dp[r-1][c] + dp[r][c-1]
                # dp 内本身是0 这句不用加
                # else:
                #     dp[r][c] = 0
        return dp[-1][-1]

sol = Solution()
re = sol.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
print(re)