class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # given array candies
        # candies [i] = # of candies kid has
        # int extraCandies = # of extra candies
        # return boolean array for all the kids, result[i] is true
        ans = []
        mostCandies = False
        kidMax = 0
        for i in range(len(candies)):
            kidMax = max(candies)
            kidAndExtraCandies = candies[i] + extraCandies
            if kidAndExtraCandies >= kidMax:
                mostCandies = True
            else:
                mostCandies = False
            ans.append(mostCandies)
        return ans
            
                