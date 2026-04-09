class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if s == t: return True
        newdict = {}
        for let in s:
            if let not in newdict:
                newdict[let] = 1
            else: 
                newdict[let] += 1
        for ter in t:
            if ter not in newdict:
                return False
            else:
                newdict[ter] -= 1
        for val in newdict.values():
            if val > 0:
                return False
        return True