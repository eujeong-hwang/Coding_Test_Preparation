class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInteger= {'I':1, 'IV':4, 'V': 5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D': 500, 'CM':900, 'M':1000}
            
        cursor = 0
        roman = 0
        
        while cursor < len(s):
            # Check current character and next character
            # We use (cursor+1) != len(s) to pass the last roman numerals to the else statement
            if (cursor+1)!= len(s) and s[cursor]+s[cursor+1] in romanToInteger:
                roman += romanToInteger[s[cursor] + s[cursor+1]]
                cursor +=2
            else:
                roman += romanToInteger[s[cursor]]
                cursor+=1
        
        return roman
                
hello = Solution()
print(hello.romanToInt("MCMXCIV"))