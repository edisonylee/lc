class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for s in tokens:
            if s not in operators:
                stack.append(s)
            else:
                second_element = int(stack.pop())
                first_element = int(stack.pop())

                if s == "+":
                    stack.append(first_element + second_element)
                if s == "-":
                    stack.append(first_element - second_element)
                if s == "*":
                    stack.append(first_element * second_element)
                if s == "/":
                    stack.append(first_element / second_element)
        return int(stack[-1])
                


