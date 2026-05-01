class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hS, hT = defaultdict(int), defaultdict(int)
        for i,l in enumerate(s):
            hS[l] +=1
            hT[t[i]] += 1
        return hS == hT