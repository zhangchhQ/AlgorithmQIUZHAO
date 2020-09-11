# hashtab two sum
# class Solution:
#     def twoSum(self, nums, target):
#         re_dict = {}
#         for ind, num in enumerate(nums):
#             re_dict[num] = ind
#         for i, v in enumerate(nums):
#             v2 = target - v
#             j = re_dict.get(v2)
#             if j and j != i:
#                 return [i, j]
class Solution:
    def twoSum(self, nums, target: int):
        if len(nums) < 2:
            return []
        re_dict = {}
        for ind, num in enumerate(nums):
            re_dict[num] = ind
        for i, k in enumerate(nums):
            k_ = target - k
            j = re_dict.get(k_)
            if j and j != i:
                return [i,j]
        return []

sol = Solution()
re = sol.twoSum([2,7,11,15],9)
print(re)
