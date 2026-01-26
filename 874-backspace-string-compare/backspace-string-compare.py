class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                else:
                    if stack:
                        stack.pop()
            return "".join(stack)
        stringS = build(s)
        stringT = build(t)
        return stringS == stringT