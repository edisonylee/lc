from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimization: If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False
            
        dic = defaultdict(int)
        dicTee = defaultdict(int)
        
        # Loop through first string
        for char in s:
            dic[char] += 1  # Just increment; defaultdict handles the rest
            
        # Loop through second string
        for char in t:
            dicTee[char] += 1
            
        return dic == dicTee