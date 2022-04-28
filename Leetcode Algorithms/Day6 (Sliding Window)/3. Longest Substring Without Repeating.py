# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# April 26, 2022

# Explanation:

# We keep increasing the end of window until we find unique elements in the string. Also, we'll calculate the max_length of the window.
# As soon as we encounter a repeated character, our start of the window should be after the first occurance of this character.
# Example: pwwkew.
# Initially window_start = 0. At window_end = 2, we find that "w" is repeated.
# We need to skip the elements "p" & "w" and get a new window_start = mapping[s[window_end]] + 1.
# If we encounter "p" later, our max condition in if block will know that i=0 needs to be ignored.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window_start = 0
        mapping = {}
        
        for window_end in range(len(s)):
            if s[window_end] in mapping:            
                window_start = max(window_start, mapping[s[window_end]]+1)
            mapping[s[window_end]] = window_end
            max_length = max(max_length, window_end - window_start + 1)                 
        return max_length

ls = Solution()
print(ls.lengthOfLongestSubstring("abcabcbb"))
print(ls.lengthOfLongestSubstring("bbbbbb"))
print(ls.lengthOfLongestSubstring("pwwkew"))


# hash table 쓰는게 더 빠르당
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         used = {}
#         max_length = start = 0
#         for i, c in enumerate(s):
#             if c in used and start <= used[c]:
#                 start = used[c] + 1
#             else:
#                 max_length = max(max_length, i - start + 1)
#             used[c] = i

#         return max_length