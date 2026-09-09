class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {"]":"[", "}":"{", ")":"("}

        for i in s:
            if i in closing:
                if not stack or stack[-1] != closing[i]:
                    return False
                else:
                    stack.pop()
            else: 
                stack.append(i)
        
        return len(stack) == 0
        