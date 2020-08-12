class Solution:
    def maximalSquare(self, matrix) -> int:
        # 1. subproblem 找元素上方和右侧中最小边数加上1
        # 2. 同维度的矩阵 每个元素表示元素周围最短边的长度
        # 3. 推导式：dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
        if not matrix:
            return 0
        h = len(matrix)
        w = len(matrix[0])
        dp = [[0 for _ in range(w)] for _ in range(h)]
        max_side = float('-inf')
        for i in range(h):
            for j in range(w):
                if matrix=='1':
                    if i == 0 or j == 0:
                        dp[i][j] = int(matrix[i][j])
                    # elif i == 0:
                    #     dp[i][j] = int(dp[i-1][j]) + int(matrix[i][j])
                    # elif j == 0:
                    #     dp[i][j] = int(dp[i][j-1]) + int(matrix[i][j])
                    else:

                            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

                max_side = max(dp[i][j], max_side)
        return max_side**2

sol = Solution()
re = sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(re)