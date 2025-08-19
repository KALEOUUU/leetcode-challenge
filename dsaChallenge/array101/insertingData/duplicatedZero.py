class Solution:
    def duplicateZeros(self, arr):
        i = 0
        n = len(arr)
        
        while i < n:
            if arr[i] == 0:
                for j in range(n-1, i, -1):
                    arr[j] = arr[j-1]
                if i + 1 < n:
                    arr[i+1] = 0
                i += 2  #
            else:
                i += 1
                
        return arr
