class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        for c in s:
            if c != "#":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
            stringOne = "".join(stack)
        for c in t:
            if c != "#":
                stack2.append(c)
            else:
                if stack2:
                    stack2.pop()
            stringTwo = "".join(stack2)
        return stringOne == stringTwo