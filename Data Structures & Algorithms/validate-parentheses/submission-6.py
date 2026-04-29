class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []

        for p in s:
            if p in valid:
                # print(stack)
                # print(p,valid[p], stack)
                if not stack or valid[p] != stack.pop():
                    return False
            else:
                stack.append(p)
        return True if not stack else False