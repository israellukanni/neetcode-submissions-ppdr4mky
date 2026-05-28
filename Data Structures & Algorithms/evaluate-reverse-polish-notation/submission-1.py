class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [tokens[0]]
        i = 1
        ops = set(["+", "-","*","/"])
        while len(stack) > 0 and i < len(tokens): 
            
            print(stack)
            if tokens[i] in ops:
                sec, fir = stack.pop(), stack.pop()
                newval = int(eval(fir + tokens[i] + sec))
                print(newval)
                stack.append(str(newval))
                i += 1
            else:
                stack.append(tokens[i])
                i +=1
        return int(stack[0])