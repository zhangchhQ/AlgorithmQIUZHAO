class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        len_num = len(nums)
        a = [[0 for _ in range(2)] for _ in range(len_num)]
        # 建两个状态的初始值
        a[0][0] = 0
        a[0][1] = nums[0]
        for i in range(1, len_num):
            # 第i个偷
            a[i][1] = a[i - 1][0] + nums[i]
            # 第i个不偷
            a[i][0] = max(a[i - 1][0], a[i - 1][1])  # i-1时的最优解
        return max(a[-1][0], a[-1][1])

sol = Solution()
re = sol.rob([1, 2, 3, 1])

