class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # given array candies
        # candies [i] = # of candies kid has
        # int extraCandies = # of extra candies
        # return boolean array for all the kids, result[i] is true
        ans = [False] * len(candies)
        mostCandies = False
        kidMax = 0
        for i in range(len(candies)):
            kidMax = max(candies)
            kidAndExtraCandies = candies[i] + extraCandies
            if kidAndExtraCandies >= kidMax:
                ans[i] = True
            else:
                ans[i] = False
        return ans
            
                