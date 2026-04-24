class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        num1, num2 = 1,2
        for i in range(2,n):
            temp = num1 + num2
            num1 = num2
            num2 = temp
        return num2