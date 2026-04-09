class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #start from the end and go backwards, subtract current num from target
        # then check if remainder is in list
        i = len(numbers) -1
        j = 0 
        while i > 0:
            if (numbers[i] + numbers[j]) == target: return [j+1,i+1]
            if (numbers[i] + numbers[j]) < target: j += 1
            if (numbers[i] + numbers[j]) > target: i -= 1
            
                    
