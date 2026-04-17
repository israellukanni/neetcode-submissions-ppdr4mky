class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) %2 != 0:
            return False
        valid = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        stack = []


        for p in s:
            if p in valid:
                stack.append(p)
            else:
                # if not stack
                if not stack or p != valid[stack.pop()]:
                    return False
        if stack:
            return False
        return True
