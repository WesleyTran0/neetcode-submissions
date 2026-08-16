class Solution:
    def isPalindrome(self, s: str) -> bool:

        validated = ""
        
        for idx in range(len(s)):
            if s[idx].isalnum():
                validated += s[idx]
                
        length = len(validated)

        for idx in range(length//2):

            print(f"begin: " + validated[idx] + " end: " + validated[length - idx - 1])
            if validated[idx].lower() != validated[length - idx - 1].lower():
                return False
        
        return True