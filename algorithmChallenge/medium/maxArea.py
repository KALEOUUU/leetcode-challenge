class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_area = max(max_area, width * current_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

height = [1, 2, 1, 2]
print(Solution().maxArea(height))