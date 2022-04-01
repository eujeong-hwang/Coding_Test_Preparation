# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 더 빨리 하는 방법이 어딨을까..., DP 유튜브 좀 봐야겠다.. dp뭐임...
# divide and conquer도 좀 보고 구현 좀 해봐야겠다ㅠㅠㅠㅠ
from typing import List
class Solution():
    def maxProfit(self, prices:List[int])->int:
        price_min = 10000
        profit = 0

        for price_current in prices:
            price_min = min(price_current, price_min)
            profit = max(profit, price_current - price_min)
        return profit

# min(a,b) function in python
# https://thepythonguru.com/python-builtin-functions/min/
# 외우기    
min("abcDEF") # find smallest item in the string
'D' # 대문자가 소문자보다 작음 ~~ 

min([2, -1, 4, 3]) # find smallest item in the list
-1

min(("one", "two", "three")) # find smallest item in the tuple
'one'

min({1: "one", 2: "two", 3: "three"}) # find smallest item in the dict
1