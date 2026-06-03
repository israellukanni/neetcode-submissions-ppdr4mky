class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        pos_speed = [(p,s) for p,s in zip(position,speed)]
        pos_speed.sort()
        # print(pos_speed)
        for p,s in pos_speed[::-1]:
            # print(stack, p,s)
            dist = target - p
            if not stack:
                stack.append(dist/s)
            else:
                # print(stack[-1], dist/s)
                if dist/s > stack[-1]:
                    stack.append(dist/s)
        return len(stack)


