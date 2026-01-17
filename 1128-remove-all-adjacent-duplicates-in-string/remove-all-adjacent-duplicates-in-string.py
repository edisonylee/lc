class Solution:
    def removeDuplicates(self, s: str) -> str:
        #1. Create a stack
        #2. If the first element (on the stack) is equal to the current character, pop it.
        #3. Else, add it to the stack.
        #4. Return a string after all removals have been made. 

        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)