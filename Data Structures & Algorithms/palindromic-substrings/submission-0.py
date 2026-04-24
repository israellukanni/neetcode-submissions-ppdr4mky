class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for i,l in enumerate(s):
            count += 1
            curr = l
            while i + 1 < len(s):
                curr += s[i + 1]
                if curr == curr[::-1]:
                    count += 1
                i += 1
        return count
