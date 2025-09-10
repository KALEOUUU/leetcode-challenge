class Solution(object):
    def findMedianofSortedArray(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        
nums1 = [1, 3, 4, 5]
nums2 = [9]

sol = Solution()
print(sol.findMedianofSortedArray(nums1, nums2))