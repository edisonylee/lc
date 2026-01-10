class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Given an integer array nums and an integer k, 
        # Return the k most frequent elements
        # You may return the answer in any order.
        count = {} # first we initialize hashmap
        freq = [] # initiliaze an empty list  = [[], [3],[2] ,[1] ,[] ,[] ]
        for _ in range(len(nums) + 1): # loop through our nums populate our freq with [[], [], [], []]
            freq.append([]) # add []
        for n in nums: # loop through nums
            count[n] = 1 + count.get(n, 0) # add one to existing value
        for n,c in count.items(): #loop through our whole hashmap
            freq[c].append(n) # at the frequency, we're going to append the numb
        res = [] # answer array
        for i in range(len(freq) - 1, 0, -1): # starting from the end, let's add the num to the ans
            for n in freq[i]: # this goes through the actual list from the end and append's the value
                res.append(n) #append the value to ans
                if len(res) == k: # one we reach k, we can exit
                    return res # return ans