class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""
        
        for i,l in enumerate(s):
            j = len(s)
            
            # print(curr)
            while j > i:
                curr = s[i:j]
                if curr == curr[::-1]:
                    if len(curr) > len(longest):
                        longest = curr
                    break
                j -= 1
        return longest