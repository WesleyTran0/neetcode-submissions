class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(i))
        return stack.pop()