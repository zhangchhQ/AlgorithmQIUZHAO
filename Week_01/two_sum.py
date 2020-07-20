class Solution:
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return []
        ret_list = []
        for i in range(len(nums)-1):

            numj = target - nums[i]
            if numj in nums[i+1:]:
                j_index = nums.index(numj, i+1)
                ret_list.extend([i, j_index])
        return ret_list

sol = Solution()
ret_list = sol.twoSum([-1,-2,-3,-4,-5], -8)
print(ret_list)