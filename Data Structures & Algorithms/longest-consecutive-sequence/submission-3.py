class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # dict
        # check if key one greater or less
        # if so, add that 
        numdict = defaultdict(int)
        maxv = 0

        for num in nums:
            if not numdict[num]:
                numdict[num] = numdict[num-1] + numdict[num+1] + 1
                numdict[num - numdict[num-1]] = numdict[num]
                numdict[num + numdict[num+1]] = numdict[num]
                maxv = max(maxv,numdict[num])
        return maxv