class Solution:
    def climbStairs(self, n: int) -> int:
        

        if n <= 2:
            return n
        prev, nex = 1,2
        for i in range(2,n):
            temp = nex
            nex = prev + nex
            prev = temp
        return nex