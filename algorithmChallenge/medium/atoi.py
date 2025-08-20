class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            index += 1
        
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1
        
        result *= sign
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result

s = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
for i in s:
    print(Solution().myAtoi(i))