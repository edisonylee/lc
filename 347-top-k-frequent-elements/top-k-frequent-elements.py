class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        freq_list = []
        for _ in range(len(nums) + 1):
            freq_list.append([])
        for number, count in dic.items():
            freq_list[count].append(number)
        res = []
        for i in range(len(freq_list) - 1, 0, -1):
            for nums in freq_list[i]:
                res.append(nums)
                if len(res) == k:
                    return res