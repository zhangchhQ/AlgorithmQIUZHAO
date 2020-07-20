class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        ret_list = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1] and i >= 1:
                continue
            j = i + 1
            k = len(nums) - 1
            sum_num = -nums[i]
            while j < k:

                if nums[j] + nums[k] < sum_num:
                    j += 1
                elif nums[j] + nums[k] > sum_num:
                    k -= 1
                elif nums[j] + nums[k] == sum_num:

                    ret_list.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        print('ok')
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        print('ko')
                        k -= 1
                    j += 1
                    k -= 1
        return ret_list


sol = Solution()
nums = [0, 0, 0, 0]
ret_list = sol.threeSum(nums)
print(ret_list)