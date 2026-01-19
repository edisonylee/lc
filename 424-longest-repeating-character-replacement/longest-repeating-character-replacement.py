class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Inputs: string, integer
        # Return the length of the longest substring containing the same letter you can get after performing the above operations.

        # Rephrase: I want to look at string, substitute at most k values to get the longest substring with the same letter.

        # Make a frequency count of the string and replace the other values that aren't the highest frequency with the highest frequency value.

        count = {} # init hashmap
        res = 0 # init ans
        l = 0 # init left pointer
        for r in range(len(s)): # loop thru with right
            count[s[r]] = 1 + count.get(s[r], 0) # create freq table
            while (r - l + 1 ) - max(count.values()) > k: # while length of the window - most appeared value > k
                count[s[l]] -= 1 # we remove the value of the left most pointer and shift it up by 1
                l += 1 # until the condition is not true
            res = max(res, r - l + 1) # return the length of the longest string
        return res # return res


