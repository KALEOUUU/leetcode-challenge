class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: List[int]
        :type l2: List[int]
        :rtype: List[int]
        """
        carry = 0
        result = []
        
        while l1 or l2 or carry:
            val1 = l1.pop() if l1 else 0
            val2 = l2.pop() if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            result.append(total % 10)

        return result[::-1]

l1 = [2,4,3]
l2 = [5,6,4]
print(Solution().addTwoNumbers(l1, l2))