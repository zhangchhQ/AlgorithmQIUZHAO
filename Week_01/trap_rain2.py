class Solution:
    def trap(self, height) -> int:
        if not height and len(height) < 3:
            return 0
        left, right = 0, len(height)-1
        # 最高柱子
        l_max, r_max = height[left], height[right]
        volume = 0
        while left < right:
            # 更新最大柱子
            l_max, r_max = max(l_max, height[left]), max(r_max, height[right])
            # 出现可盛水条件 更新盛水数量
            if l_max <= r_max:
                volume += (l_max - height[left])
                left += 1
            else:
                volume += (r_max - height[right])
                right -= 1

        return volume

sol = Solution()
sol.trap([2,0,2])
