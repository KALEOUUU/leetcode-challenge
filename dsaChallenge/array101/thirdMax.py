class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = set(nums)
        if len(unique_nums) < 3:
            return max(unique_nums)
        
        unique_nums.remove(max(unique_nums))
        unique_nums.remove(max(unique_nums))
        
        return max(unique_nums)