class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sumLeft = [0] * len(nums)
        
        for i in range(1, len(nums)):
            sumLeft[i] = sumLeft[i - 1] + nums[i - 1]
        
        total_sum = sum(nums)
        for i in range(len(nums)):
            if sumLeft[i] == total_sum - sumLeft[i] - nums[i]:
                return i
            
        return -1

nums = [1, 7, 3, 6, 5, 6]
print(Solution().pivotIndex(nums))