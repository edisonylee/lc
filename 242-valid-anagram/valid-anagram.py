class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for chr in s: # store letters and their counts
            if chr in dic:
                dic[chr] += 1
            else:
                dic[chr] = 1
        for chr in t:
            if chr in dic:
                dic[chr] -= 1
                if dic[chr] < 0:
                    return False
            else:
                return False
        return True