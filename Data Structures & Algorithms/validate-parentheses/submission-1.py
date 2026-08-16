class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        for paren in s:
            if paren in pairs:
                if len(stack) == 0 or stack[-1] != pairs[paren]:
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(paren)
        
        return len(stack) == 0