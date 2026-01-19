class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Return True if s2 contains a permutation of s1, False otherwise
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)): # Initialize frequency counts
            s1_count[ord(s1[i]) - ord('a')] += 1 # i.e., 97 - 97, = 0,a=0
            window_count[ord(s2[i]) - ord('a')] += 1
        if s1_count == window_count: # Window is a permutation
            return True
        for i in range(len(s1), len(s2)):
            window_count[ord(s2[i]) - ord('a')] += 1
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if s1_count == window_count:
                return True
        return False
