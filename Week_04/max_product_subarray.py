class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0
        per_max = nums[0]
        per_min = nums[0]
        res_max = nums[0]
        for num in nums[1:]:
            # per_max = max(per_max*num, per_min*num, num)
            # per_min = min(per_max*num, per_min*num, num)
            # res_max = max(res_max, per_max)
            cur_max = max(per_max*num, per_min*num, num)
            cur_min = min(per_max*num, per_min*num, num)
            res_max = max(res_max, cur_max)
            per_min = cur_min
            per_max = cur_max
        return res_max

sol = Solution()
sol.maxProduct([2,3,-2,4, 22, 1, -4])