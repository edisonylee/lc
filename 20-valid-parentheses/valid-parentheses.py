class Solution:
    def isValid(self, s: str) -> bool:
        #Valid if brackets are closed by same brackets
        stack = [] # Initialize our stack
        matching = {"(": ")", "[": "]", "{": "}"} # Create a dictionary to look for the opening parentheses

        for c in s: # Loop through 
            if c in matching: # If an opening bracket, append it
                stack.append(c) # Append c to stack
            else:
                if not stack: # If that stack is already empty, we can return False
                    return False
                previous_opening = stack.pop() # get's the last opening
                if matching[previous_opening] != c: # if the closing bracket of the last opening is not the current c, return False
                    return False
        return not stack # Return True if stack empty
                    
