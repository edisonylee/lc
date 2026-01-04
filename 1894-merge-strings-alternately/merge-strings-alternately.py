class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Given 2 strings, merge them by adding them in alternating order (start with word 1)
        # Append the additional letters on the longer string to the end of the merged string.
        ans = []
        # While str1 < str2
        # "abc" and "pqr"
        # "ab" "pqc"
        # [a,p,b,q,]
        i = j = 0 # set up two pointers
        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            j += 1
            i += 1
        while i < len(word1):
            ans.append(word1[i])
            i += 1
        while j < len(word2):
            ans.append(word2[j])
            j += 1
        return "".join(ans)
            