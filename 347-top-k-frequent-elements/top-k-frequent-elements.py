class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Use a hashmap to store frequency.
        # 2. Place these frequencies in a list of buckets.
        # 3. Loop through from the end, and append to our ans. 

        dic = {} # 1. frequency hashmap
        for num in nums: 
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        freq = [] # 2. build our empty buckets
        for _ in range(len(nums) + 1): # [0, 1, 1, 3, 4, 5] -> [[], [0, 1, 3, 4, 5], [2], [], [], []]
            freq.append([])
        for num, count in dic.items(): # 3. Add nums to our array, i.e., (1,1,3,3) gives us...
            freq[count].append(num) # -> [[], [], [3, 1], [], []]

        ans = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        

