import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        numset = set(nums) #{2,20,4,10,3,4,5}
        start = [] #[2,20,10]
        for nu in numset:
            if (nu - 1) not in numset:
                start.append(nu)
        track = 0 #
        for st in start:
            #new = st
            count = 1
            while (st + 1) in numset:
                count += 1
                st += 1
            track = max(track,count)
        return track 

