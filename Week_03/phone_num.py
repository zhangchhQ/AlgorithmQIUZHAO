class Solution:
    # 类似括号生成
    def letterCombinations(self, digits: str) -> List[str]:
        ret_list = []
        refer_dict = {}
        refer_dict['2'] = "abc"
        refer_dict['3'] = "def"
        refer_dict['4'] = "ghi"
        refer_dict['5'] = "jkl"
        refer_dict['6'] = "mno"
        refer_dict['7'] = "pqrs"
        refer_dict['8'] = "tuv"
        refer_dict['9'] = "wxyz"
        s = ""
        # 类括号生成问题，有几个数字就有几个格子
        deep = len(digits)
        if deep == 0:
            return []
        def generate(level, deep, s):
            # terminator
            if level >= deep:
                ret_list.append(s)
                return
            # current process
            # 类似括号问题中判断合法性的问题
            str_letter = refer_dict.get(digits[level])
            for j in str_letter:
                # drill down
                generate(level+1, deep, s+j)
        generate(0, deep, s)
        return ret_list 