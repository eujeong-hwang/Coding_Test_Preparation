# Feb 09, 2022
## Question - 121. Best Time To Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Related Topics
    Array
    Dyamic Programming

## Question

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Solution 1 
```
# Answer Code
class Solution():
    def maxProfit(self, prices:list)->int:

        price_min = 10000
        profit = 0

        for price_current in prices:
            price_min = min(price_current, price_min)
            profit = max(profit, price_current - price_min)
        return profit



# test
prices = [7, 1, 5, 3, 6, 4]
Solution.maxProfit(prices)

# Output
5

```

## What I learned - min() function in Python
    The min() function returns the smallest of the input values.

>>> 
>>> min("abcDEF") # find smallest item in the string
'D'
>>>
>>> 
>>> min([2, -1, 4, 3]) # find smallest item in the list
-1
>>> 
>>>
>>> min(("one", "two", "three")) # find smallest item in the tuple
'one'
>>> 
>>> 
>>> min({1: "one", 2: "two", 3: "three"}) # find smallest item in the dict
1
>>>
>>>
>>> min([]) # empty iterable causes ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: min() arg is an empty sequence
>>> 
>>> 
>>> min([], default=0) # supressing the error with default value
0
>>>

## What I learned - max() function in Python
    The max() function returns the largest of the input values.

>>> 
>>> max("abcDEF") # find largest item in the string
'c'
>>>
>>> 
>>> max([2, 1, 4, 3]) # find largest item in the list
4
>>> 
>>>
>>> max(("one", "two", "three")) # find largest item in the tuple
'two'
>>> 
>>> 
>>> max({1: "one", 2: "two", 3: "three"}) # find largest item in the dict
3
>>>
>>>
>>> max([]) # empty iterable causes ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: max() arg is an empty sequence
>>> 
>>> 
>>> max([], default=0) # supressing the error with default value
0
>>>