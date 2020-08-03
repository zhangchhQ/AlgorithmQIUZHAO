class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(n):
            if n == 0:
                return 1
            half = fast_pow(n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        if n < 0:
            x = 1/x
            n = -n
        return fast_pow(n)

sol = Solution()
sol.myPow(3, 10)
