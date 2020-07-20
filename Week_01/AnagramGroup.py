class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. 遍历一遍
        # 2.
        re_dict = {}
        for item in strs:
            # 排序完的不变数组
            key = tuple(sorted(item))
            # 需要列表套列表的形式
            # 这样不行 dict.get()的返回值是list， type是Nonetype
            # re_dict[key] = re_dict.get(key, []).append([item])
            re_dict[key] = re_dict.get(key, []) + [item]
        return list(re_dict.values())