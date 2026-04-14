class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # dict
        # check if key one greater or less
        # if so, add that 
        numset = set(nums)
        numdict = defaultdict(int)
        maxv = 0
        for num in nums:
            if num - 1 in numset:
                continue
            count = 1
            curr = num
            while curr + 1 in numset:
                count += 1
                curr +=1
            # numdict[num] = count
            maxv = max(maxv,count)

        return maxv