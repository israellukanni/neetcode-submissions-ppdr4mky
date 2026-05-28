class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [tokens[0]]
        i = 1
        ops = set(["+", "-","*","/"])
        while len(stack) > 0 and i < len(tokens): 
            print(stack)
            if tokens[i] in ops:
                sec, fir = int(stack.pop()), int(stack.pop())
                newval = 0
                if tokens[i] == "+":
                    newval = str(fir+sec)
                elif tokens[i] == "-":
                    newval = str(fir-sec)
                elif tokens[i] == "*":
                    newval = str(fir*sec)
                else:
                    newval = str(int(float(fir)/sec))
                print(newval)
                # newval = int(eval(fir + tokens[i] + sec))
                stack.append(newval)
                i += 1
            else:
                stack.append(tokens[i])
                i +=1
        return int(stack[0])