from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int) # init hashmap
        for num in nums: # add numbers to hashmap
            dic[num] += 1
        sorted_items = sorted(dic.items(), key=lambda x:x[1], reverse = True)
        result = []
        for pair in sorted_items:
            num = pair[0]
            result.append(num)
            if len(result) == k:
                break
        return result

        