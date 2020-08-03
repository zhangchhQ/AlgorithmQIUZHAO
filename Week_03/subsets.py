class Solution:
    def subsets(self, nums: list):
        # 先放一个初始值
        result = [[]]
        # 把nums中每一个数加到result中的每一个子集中，更新当前的子集结果。
        for num in nums:
            result = result + [[num] + subset for subset in result]
        return result
