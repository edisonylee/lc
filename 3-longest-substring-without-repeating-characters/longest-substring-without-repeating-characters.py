class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        substring_set = set()
        for right in range(len(s)):
            while s[right] in substring_set:
                substring_set.remove(s[left])
                left += 1
            substring_set.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
        
# So, if the string has found a duplicate, that means that we can get the length of the string (right - left)
# And with that, we can compare the two strings. 

# Can we just compare the strings without appending two different strings?
# Maybe, but first let's just make the two strings