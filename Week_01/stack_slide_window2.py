class Solution:
    def maxSlidingWindow(self, nums, k: int):
        # 如果加入的是最大 更新滑窗内最大 如果掉队的是最大 在滑窗中再找一个最大
        if len(nums) < k:
            return
        res = []
        max_temp = max(nums[:k])
        for i in range(len(nums)-k):
            res.append(max_temp)
            if nums[i+k] > max_temp:
                max_temp = nums[i+k]
            else:
                if nums[i] == max_temp:
                    max_temp = max(nums[i+1:i+k+1])
        res.append(max_temp)
        return res
sol = Solution()
sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)