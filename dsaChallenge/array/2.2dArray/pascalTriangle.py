class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        triangle = []
        
        for row in range(numRows):
            current = [1] * (row + 1)
            for col in range (1, row):
                current[col] = triangle[row-1][col-1] + triangle[row-1][col]
            triangle.append(current)
        
        return triangle

print(Solution().generate(5))
        