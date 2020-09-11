class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs
        s = ''
        ret_list = []
        def generate(left, right, n, s):
            if right == n and left == n:
                ret_list.append(s)
                return
            if left < n:
                # 左侧合法向左走
                generate(left+1, right, n, s+'(')
            if right < left:
                # 右侧合法向右走
                generate(left, right+1, n, s+')')
        generate(0, 0, n, s)
        return ret_list