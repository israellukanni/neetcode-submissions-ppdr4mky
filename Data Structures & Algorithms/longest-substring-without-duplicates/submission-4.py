class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0, 1
        maxString = 0
        # curr= s[0]]
        curr = s[l:r]
        while r < len(s):
            curr = s[l:r]
            if s[r] in curr:
                l +=1
                continue
            else:
                curr += s[r]
            
            maxString = max(maxString,len(curr))
            # print(curr, maxString)
            r += 1
            
        return max(maxString,len(curr))