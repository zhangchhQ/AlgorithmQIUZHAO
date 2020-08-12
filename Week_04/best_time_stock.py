class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        dp = [0 for i in range(len(prices))]
        dp[0] = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[-1]

sol = Solution()
re = sol.maxProfit([7,1,5,3,6,4])
print(re)