class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s: # loop through string
            if stack and stack[-1] == c:#if stack is non empty and the first element is c # pop
                stack.pop()
            else:
                stack.append(c) # appends if the first element at the top is not equal to c 
        return "".join(stack) # return a string 