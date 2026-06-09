class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)
        for s in strs:
            sortS = "".join(sorted(s))
            anagrams[sortS].append(s)
        return list(anagrams.values())