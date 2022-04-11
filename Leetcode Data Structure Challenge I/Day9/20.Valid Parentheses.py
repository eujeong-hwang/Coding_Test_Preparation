# https://leetcode.com/problems/valid-parentheses/

# 20ms (처음에 채점할 떄는 69ms인데 다시 해보니 20ms.. 뭐즤...)
class Solution:
    def isValid(self, s: str) -> bool:
        d = {')' : '(', '}' : '{', ']' : '['}
        stack1 = ['N']
        
        for i in s:
            if i in d.keys():
                if stack1.pop() != d[i]:
                    return False
            else:
                stack1.append(i)
        
        return len(stack1) == 1

vp = Solution()
print(vp.isValid('([{}])'))


# 43 ms
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={'}':'{',')':'(',']':'['}
        for i in s:
            if i in brackets.values(): # Opening bracket
                stack.append(i)
            else:# Closing bracket
                if stack and brackets[i]==stack[-1] :  
                    stack.pop()
                else: 
                    return False
        
        if stack:
            return False
        return True