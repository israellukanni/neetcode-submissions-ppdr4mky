class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        check = 0
        maxString = 0
        for i,l in enumerate(s):
            curr = l
            check = i + 1
            while check < len(s) and s[check] not in curr:
                curr += s[check]
                check +=1
            maxString = max(maxString,len(curr))
        return maxString