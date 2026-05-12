class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        trips = []
        nums.sort()

        for i, n in enumerate(nums):

            if n > 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums)-1
            while l < r:
                if n + nums[l] + nums[r] == 0:
                    trips.append([n,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l +=1
                elif n + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -=1
        return trips
