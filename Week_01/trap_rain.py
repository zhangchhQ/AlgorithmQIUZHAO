class Solution:
#     def trap(self, height):
#         left = 0
#         right = len(height)-1
#         temp, total, high = 0,0,1
#         while left <= right:
#             while left <= right and height[left] < high:
#                 # 记录柱子
#                 total += height[left]
#                 left += 1
#             while left <= right and height[right] < high:
#                 total += height[right]
#                 right -= 1
#             high += 1
#             # 更新面积
#             # 每次只有一层　不用 *high
#             temp += (right - left +1)
#         return temp - total
    def trap(self, bars):
        if not bars or len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume

sol = Solution()
ret = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(ret)
