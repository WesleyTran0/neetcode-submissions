class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        for paren in s:
            if paren in pairs:
                if not stack or stack[-1] != pairs[paren]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(paren)
        
        return True if not stack else False