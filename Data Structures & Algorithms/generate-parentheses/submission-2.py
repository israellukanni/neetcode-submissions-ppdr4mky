class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def dfs(lp, rp):
            
            if lp == rp == n:
                res.append("".join(stack))
                return 
            
            if lp < n:
                stack.append("(")
                dfs(lp+1,rp)
                stack.pop()
            if rp < lp:
                stack.append(")")
                dfs(lp, rp+1)
                stack.pop()
        dfs(0,0)
        return res
            
