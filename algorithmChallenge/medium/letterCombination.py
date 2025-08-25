class Solution(object):
    def letterCombination(self, digits):
        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        result = ['']
        for digit in digits:
            letters = digits_to_letters.get(digit, '')
            result = [prefix + letter for prefix in result for letter in letters]
        return result
