class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # 钱数相当于上多少级台阶，动归要在前面多留出一个空位
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            # 当coin==2 他对2之前的不会有影响
            for x in range(coin, amount+1):
                # 原先方法和新方法二选一
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1




sol = Solution()
re = sol.coinChange([1, 2, 5], 11)
print(re)
