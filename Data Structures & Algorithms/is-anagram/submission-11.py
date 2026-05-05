class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        hs,ht = defaultdict(int),defaultdict(int)

        for i,(ss,tt) in enumerate(zip(s,t)):
            hs[ss] +=1
            ht[tt] += 1
        return hs == ht