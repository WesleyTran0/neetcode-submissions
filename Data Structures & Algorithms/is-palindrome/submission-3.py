class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        stripped = ""
        for c in s:
            if c.lower() in "abcdefghijklmnopqrstuvwxyz0123456789":
                stripped += c.lower()
        
        l, r = 0, len(stripped) - 1

        while l < r:
            if stripped[l] != stripped[r]:
                return False

            l += 1
            r -= 1
        
        return True