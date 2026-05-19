class Solution:
    def climbStairs(self, n: int) -> int:
        
        # memo = defaultdict(int)
        # memo[1] = 1
        # memo[2] = 2
        # if n < 3:
        #     return memo[n]
        # for i in range(3,n):
        #     memo[i] = memo[i-1] + memo[i-2]
        # return memo[n-1] + memo[n-2]

        f,s = 1,1
        for i in range(n-1):
            temp = s
            s += f
            f = temp
        return s
