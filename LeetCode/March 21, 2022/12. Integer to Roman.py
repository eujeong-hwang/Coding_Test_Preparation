# https://leetcode.com/problems/integer-to-roman/
# Medium

class Solution:
    def intToRoman(self, num: int) -> str:
        intToRoman = {'1' : 'I', '4': 'IV', '5': 'V', '9': 'IX', '10': 'X', '40': 'XL', 
'50': 'L', '90': 'XC', '100': 'C', '400': 'CD', '500':'D', '900': 'CM', '1000': 'M'}

        cursor = 0
        RomanValue = ""
        IntVal = 0

        while cursor < num:
            IntVal += num[cursor] * (10**(len(num)-1)) 
            if IntVal in intToRoman:
                RomanValue = intToRoman[IntVal]
            else:
                
