class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 3,4,5,6   1,2
        l, r = 0,len(nums)-1
        
        
        while(l<r):
            mid = l + (r-l)//2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        l, r = 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]> target:
                r = mid -1
            else:
                l = mid + 1
        return -1
        

        