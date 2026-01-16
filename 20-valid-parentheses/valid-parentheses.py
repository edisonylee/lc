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
                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False
        return not stack # Return True if stack empty
                    
