class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        diagonal = {}
        
        for r in range(m):
            for c in range(n):
                if r + c not in diagonal:
                    diagonal[r + c] = []
                diagonal[r + c].append(mat[r][c])
                
        result = []
        
        for diag in range(m + n -1):
            if diag % 2 == 0:
                result.extend(diagonal[diag][::-1])
            else:
                result.extend(diagonal[diag])
                
        return result
    
mat = [[1,2,3],[4,5,6],[7,8,9]]

print(Solution().findDiagonalOrder(mat))
        
        