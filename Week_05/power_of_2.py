class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        if n < 0:
            return False
        while n:
            n = n & (n-1)
            count += 1
        if count == 1:
            return True
        return False
