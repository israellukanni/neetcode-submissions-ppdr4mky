class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS,hashT = defaultdict(int), defaultdict(int)

        for l in s:
            hashS[l] += 1
        for l in t:
            hashT[l] += 1
        return hashS == hashT