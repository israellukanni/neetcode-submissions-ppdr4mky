class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ""
        for l in s:
            if l.isalnum():
                cleanS += l.lower()
        
        return cleanS == cleanS[::-1]