class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for s in tokens:
            if s not in operators:
                stack.append(s)
            else:
                second_element = stack.pop()
                first_element = stack.pop()

                if s == "+":
                    stack.append(int(first_element) + int(second_element))
                if s == "-":
                    stack.append(int(first_element) - int(second_element))
                if s == "*":
                    stack.append(int(first_element) * int(second_element))
                if s == "/":
                    stack.append(int(first_element) / int(second_element))
        return int(stack[-1])
                


