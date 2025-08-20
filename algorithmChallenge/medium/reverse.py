class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        reversed_x = 0

        while x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        reversed_x *= sign
        return reversed_x if -2**31 <= reversed_x <= 2**31 - 1 else 0

x = [123, -123, 120]
for i in x:
    print(Solution().reverse(i))