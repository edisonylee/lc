class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # Store indices of temperatures
        
        for i in range(n):
            # While stack is not empty and current temp is warmer than stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)
        
        return ans