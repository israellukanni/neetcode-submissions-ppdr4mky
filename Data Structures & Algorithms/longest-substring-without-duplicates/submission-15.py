class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        # l, r =  0, 1
        contained = set(s[0])
        maxLen = 1
        # curr = 1
        l = 0
        for r in range(1,len(s)):
            
            while l < r and s[r] in contained:
                contained.remove(s[l])
                l += 1
            contained.add(s[r])
            maxLen = max(maxLen, len(contained))
            
        return maxLen


            