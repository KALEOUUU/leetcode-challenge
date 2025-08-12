class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix:
            return []
        
        response = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # col
            for col in range(left, right + 1):
                response.append(matrix[top][col])
            top += 1
            
            # row
            for row in range(top, bottom + 1):
                response.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                for col in range(right, left -1, -1):
                    response.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top -1, -1):
                    response.append(matrix[row][left])
                left += 1
        
        return response

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix))
            
            
                
        