class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Check if the length of the strings are the same 
            return False # Return False if they are not the same

        countS, countT = {}, {} # Create Hash Sets

        for i in range(len(s)): # Go through the strings at the same time because they're the same legnth
            countS[s[i]] = 1 + countS.get(s[i], 0) # Counting the occurences of each occurence 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT # Return true if the counts are the same 

    
