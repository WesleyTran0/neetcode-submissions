class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mp = {"}": "{", ")": "(", "]": "["}
        for i in s:
            if i in mp:
                if len(stack) == 0 or stack.pop() != mp[i]:
                    return False
            else: 
                stack.append(i)
        
        return len(stack) == 0
