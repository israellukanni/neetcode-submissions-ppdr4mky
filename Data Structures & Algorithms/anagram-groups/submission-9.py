class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        for st in strs:
            hashy["".join(sorted(st))].append(st)
        
        return list(hashy.values())