class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # So, given two strings, s and t, return true if t is an anagram of s,
        # And false otherwise
        # So, what is an anagram?
        # An anagram is any string that contains all the letters, however mixed up, as another string
        # With this in mind, we can start our implementation.
        # Initial approach: Create dictionaries for each each string, then we can compare them by using .items
        # This will allow us to fetch the appropriate key, value pairs. We can either loop through and compare 
        # with a for loop, or just do the == for the hashMaps. 
        # Let's try both out.
        dicS = {}
        dicT = {}
        for chr in s:
            if chr in dicS:
                dicS[chr] += 1
            else: 
                dicS[chr] = 1
        for chr in t:
            if chr in dicT:
                dicT[chr] += 1
            else: 
                dicT[chr] = 1
        return dicS == dicT