class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = max(nums)
        maxIndex = nums.index(m)
        
        for i, x in enumerate(nums):
            if i != maxIndex and m < 2 * x:
                return -1
        
        return maxIndex

print(Solution().dominantIndex([3, 6, 1, 0]))  
print(Solution().dominantIndex([1, 2, 3, 4]))  
            
        