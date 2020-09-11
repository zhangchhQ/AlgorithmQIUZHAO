class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        ret_list = []
        for i in range(len(nums)):
            # 整个列表排过序，当i〉0 后面的数都比nums[i]大，不可能三数和等于0，循环停止
            if nums[i] > 0:
                return ret_list
            # i 位置的去重 nums[i] 与 nums[i-1]比较 如果与i+1比较会少结果
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) -1
            target_temp = -nums[i]
            # nums[j] + nums[k] == target_temp 小了挪j 大了挪k
            while j < k:
                if nums[j] + nums[k] < target_temp:
                    j += 1
                elif nums[j] + nums[k] > target_temp:
                    k -= 1
                else:
                    ret_list.append([nums[i], nums[j], nums[k]])
                    # 去重：当数组中出现一样的值的时候会重复 nums[j] == nums[j+1] nums[k] == nums[k-1]
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return ret_list

sol = Solution()
sol.threeSum([0,0,0])