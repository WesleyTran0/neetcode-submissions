class Solution:
    def isPalindrome(self, s: str) -> bool:

        new = ""
        for i in s:
            if not i.isalnum():
                continue
            else:
                new += i
        
        l = 0
        r = len(new) - 1
        while l < r:
            if new[l].lower() != new[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True