class Solution:
    def findLucky(self, arr: List[int]) -> int:

        dic = {} 
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        max_lucky_number = -1
        for key, value in dic.items():
            if key == value:
                lucky_number = key
                max_lucky_number = max(max_lucky_number, lucky_number)

        return max_lucky_number