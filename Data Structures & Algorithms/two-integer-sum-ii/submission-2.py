class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #start from the end and go backwards, subtract current num from target
        # then check if remainder is in list
        i, j  = len(numbers) -1, 0

        while i > 0:
            curSum = numbers[i] + numbers[j]
            if (curSum) == target: return [j+1,i+1]
            if (curSum) < target: j += 1
            if (curSum) > target: i -= 1
            
                    
