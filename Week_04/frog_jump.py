class Solution:
    def canCross(self, stones) -> bool:
        n = len(stones)

        dp = [[False] * n for _ in range(n)]
        dp[0][1] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                dist = stones[i] - stones[j]
                if dist > i:
                    break
                if dp[j][dist]:
                    if i == n - 1:
                        return True
                    dp[i][dist] = dp[i][dist + 1] = dp[i][dist - 1] = True
        return False


sol = Solution()
sol.canCross([0,1,3,4,5,7,9,10,12])