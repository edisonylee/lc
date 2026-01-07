class Solution:
    def reverseVowels(self, s: str) -> str:
        # Given a string s, reverse vowels in the string and return it
        j = len(s) - 1 # end
        i = 0
        s = list(s)
        vowels = set("aeiouAEIOU")
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)



            