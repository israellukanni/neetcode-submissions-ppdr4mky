class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashS, hashT = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            hashS[s[i]] += 1
            hashT[t[i]] += 1
        return hashS == hashT