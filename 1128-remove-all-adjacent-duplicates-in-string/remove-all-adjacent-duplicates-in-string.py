class Solution:
    def removeDuplicates(self, s: str) -> str:
        #1. Create a stack
        #2. If the first element (on the stack) is equal to the current character, pop it.
        #3. Else, add it to the stack.
        #4. Return a string after all removals have been made. 

        stack = [] # Make stack
        for c in s: # Loop through stack
            if stack and c == stack[-1]: # If non-empty and top of stack is equal to c, pop 
                stack.pop()
            else: # Else, append it.
                stack.append(c)
        return "".join(stack)

        # "abbaca" -> [a] -> [a, b] -> [a,b], c to be added is b & stack[-1] = b -> [a] -> [a] a c to be added is 
        # a and stack[-1] is a -> [], stack empty so add c -> [c], [c, a]
        