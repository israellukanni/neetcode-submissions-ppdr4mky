class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        freqList = []
        for key,val in freq.items():
            freqList.append((val,key))
        freqList.sort()
        
        kFreq = []
        # print(freqList)
        while len(kFreq) < k:
            kFreq.append(freqList.pop()[1])
        
        return kFreq
        