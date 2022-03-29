# https://leetcode.com/problems/integer-to-roman/
# Medium

class Solution:
    def intToRoman(self, num: int) -> str:
#         intToRoman = {1 : 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 
# 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500:'D', 900: 'CM', 1000: 'M'}

        # RomanValue = ""
        # IntVal = 0
        # RemainderIntVal = 0

        # while cursor < num:
        #     IntVal += num[cursor] * (10**(len(num)-1)) 
        #     RemainderIntVal += num - IntVal
        #     for i in intToRoman:
        #         if RemainderIntVal < 1:

        #     if IntVal in intToRoman:
        #         RomanValue = intToRoman[IntVal]
        
        intToRoman = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        RomanValue =''

        while num != 0:
            for value in intToRoman:
                if num-value >=0:
                    print(value)
                    RomanValue += intToRoman[value]
                    num = num - value
                    break
        return RomanValue

what = Solution()
print(what.intToRoman(3))

