class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        day_len = len(prices)
        i = 0
        j = 1
        ret_num = 0
        while j <= day_len - 1:
            if prices[i] < prices[j]:
                ret_num += prices[j] - prices[i]
            i += 1
            j += 1
        return ret_num