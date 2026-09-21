class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        sol,sub = [], []

        def dfs(i):
            if i >= len(s):
                sol.append(sub.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s,i,j):
                    sub.append(s[i:j+1])
                    dfs(j+1)
                    sub.pop()
        dfs(0)
        return sol
    
    def isPalindrome(self,s, l,r):
        while l< r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
        
            