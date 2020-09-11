class Solution:
    def reversePairs(self, nums) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(nums, l, mid, r) + left + right

    def merge(self, nums, l, mid, r):
        # 找翻转对的代码
        ans = 0
        i, j = l, mid + 1
        while i <= mid and j <= r:
            if (nums[i] + 1) >> 1 > nums[j]:
                ans += (mid - i + 1)
                j += 1
            else:
                i += 1
        nums[l:r + 1] = sorted(nums[l:r + 1])
        return ans

sol = Solution()
sol.reversePairs([1,3,2,3,1])