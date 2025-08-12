class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        
nums = [1,2,3,4,5,6,7]
print(Solution().rotate(nums, 2))
