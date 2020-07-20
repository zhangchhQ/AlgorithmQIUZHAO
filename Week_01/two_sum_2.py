# hashtab two sum
class Solution:
    def twoSum(self, nums, target):
        re_dict = {}
        for ind, num in enumerate(nums):
            re_dict[num] = ind
        for i, v in enumerate(nums):
            v2 = target - v
            j = re_dict.get(v2)
            if j and j != i:
                return [i, j]


