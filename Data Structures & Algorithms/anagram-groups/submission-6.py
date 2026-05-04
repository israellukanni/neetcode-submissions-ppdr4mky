class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hs = defaultdict(list)

        for s in strs:
            sort = "".join(sorted(s))
            hs[sort].append(s)
        
        return list(hs.values())
