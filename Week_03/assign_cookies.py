class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_len = len(g)
        s_len = len(s)
        i, j, res_num = 0, 0, 0
        while i < g_len and j < s_len:
            if g[i] <= s[j]:
                res_num += 1
                i += 1
                j += 1
            else:
                j += 1
        return res_num