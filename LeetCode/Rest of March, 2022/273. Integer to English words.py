# https://leetcode.com/problems/integer-to-english-words/
# Question : Convert a non-negative integer num to its English words representation.

# Example: 1,234,567,890

# One billion, Two Hundred Thirty Four Million, 
# Five Hundred Sixty Seven Thousand, Eight Hundred Ninety

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        to19 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        # 1 billion = 10^9
        # 1 million = 10^6
        # 1 thousad = 10^3
        # 1 hundred = 10^2

        def recursor(num):
            if num == 0:
                return ""

            if num <= 19:
                return to19[num-1]
            # 17 = to19[17-1]

            if num <=99:
                return 