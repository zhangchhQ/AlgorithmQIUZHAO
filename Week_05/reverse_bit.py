class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        end = 31
        while n:
            ret += (n & 1) << end
            n = n >> 1
            end -= 1
        return ret