class Solution:
    def isValid(self, s: str) -> bool:
        
        close = {"}": "{", ")": "(", "]": "["}
        stack = []

        for i in s:
            if i in close.keys():
                if not stack or stack.pop() != close[i]:
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0