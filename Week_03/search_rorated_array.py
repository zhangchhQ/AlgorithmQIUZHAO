class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # mid 和 头元素比较
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:    # 在左侧递增数组中
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

sol = Solution()
ret = sol.search([1, 3], 3)
print(ret)
