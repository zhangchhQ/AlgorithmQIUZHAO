class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归法：
        # 0. 创建一个全局变量，作为主角
        use = {0: 1, 1: 1}
        # 创建递归主体
        def cb(n, use):
            # 1. terminator
            if n in use.keys():
                return use[n]
            # 2. process
            else:
                # drill down
                cb1 = cb(n-1,use)
                cb2 = cb(n-2, use)
                temp = cb1 + cb2
                # 3. process
                use[n] = temp
                return temp
        return cb(n, use)

sol = Solution()
sol.climbStairs(5)