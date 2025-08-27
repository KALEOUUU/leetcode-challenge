class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        numbers = list(range(1, n + 1))
        k -= 1
        permutation = []
        while n > 0:
            n -= 1
            fact = factorial(n)
            index = k // fact
            k %= fact
            permutation.append(str(numbers[index]))
            numbers.pop(index)
        return ''.join(permutation)
