class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        ret_list = [0]
        for num_s in s:
            for sub_num in ret_list:
                if sub_num == int(num_s):
                    continue
                new_num = sub_num * 10 + int(num_s)
                if new_num > 100:
                    break
                ret_list.append(sub_num*10+int(num_s))
        ret_num = 0
        s_len = len(s)
        for sub_num in set(ret_list):
            if 0 < sub_num <= 26:
                sub_len = len(sub_num)

                ret_num += 1
        return ret_num

sol = Solution()
print(sol.numDecodings('12'))

