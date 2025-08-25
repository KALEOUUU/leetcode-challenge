class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        quotient = abs(dividend) // abs(divisor)
        quotient = -quotient if negative else quotient
        return min(max(INT_MIN, quotient), INT_MAX)
