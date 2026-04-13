class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numdict = defaultdict(int)
        sortlist = []
        for num in nums:
            numdict[num] += 1
        
        for key, val in numdict.items():
            sortlist.append((val,key))
        sortlist.sort()
        answer = []
        while len(answer) < k:
            answer.append(sortlist.pop()[1])
        return answer