#  Problem :- https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

#  Solution :- https://www.youtube.com/watch?v=qtVh-XEpsJo&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=27

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxans = float("-inf")
        setx = set()
        l = 0
        for r in range(len(s)):  # outer loop for traversing the string
            if s[r] in setx:  # if duplicate element is found
                while l < r and s[r] in setx:
                    setx.remove(s[l])
                    l += 1
            setx.add(s[r])
            maxans = max(maxans, r - l + 1)
        return maxans
