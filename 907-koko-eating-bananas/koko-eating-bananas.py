class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to check if Koko can eat all bananas within h hours at given speed
        def canEatAll(speed):
            total_hours = 0
            for pile in piles:
                # Calculate hours needed for this pile (ceiling division)
                total_hours += (pile + speed - 1) // speed
                # Early termination if already exceeds h hours
                if total_hours > h:
                    return False
            return total_hours <= h
        
        # Binary search bounds
        left, right = 1, max(piles)
        
        # Binary search for minimum valid speed
        while left < right:
            mid = (left + right) // 2
            if canEatAll(mid):
                right = mid  # Try smaller speed
            else:
                left = mid + 1  # Need larger speed
        
        return left