class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = ""
        closing = {"}": "{", ")":"(", "]":"["}

        for i in s:
            if i in closing :
                if not stack or stack[-1] != closing[i]:
                    return False
                else:
                    stack = stack[:-1]
            else:
                stack += i
        
        return len(stack) == 0