class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        #  横向遍历
        length, count = len(strs), len(strs[0])
        for j in range(count):
            c = strs[0][j]
            # 不相等或长度超标 则证明寻找过程结束
            for i in range(1, length):
                if len(strs[i]) < j or strs[i][j] != c:
                    return strs[0][:j]
        return ""

sol = Solution()
sol.longestCommonPrefix(["flower","flow","flight"])