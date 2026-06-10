class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0, 1
        curr = s[:r]
        maxString = len(curr)

        while r < len(s):
            curr = s[l:r]

            if s[r] in curr:
                l += 1
                continue
            else:
                curr += s[r]
            r +=1 
            maxString = max(maxString, len(curr))
        
        return maxString