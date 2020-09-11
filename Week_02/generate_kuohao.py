class Solution:
    def generateParenthesis(self, n: int):
        ret_list = []
        s = ""

        def generate(level, max_, s):
            if level >= max_:
                print(s)
                return
            generate(level + 1, max_, s + '(')
            generate(level + 1, max_, s + ')')
            return s
        generate(0, 2 * n, s)
        return ret_list

sol = Solution()
sol.generateParenthesis(3)