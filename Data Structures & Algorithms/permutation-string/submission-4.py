class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        perm = defaultdict(int)
        for s in s1:
            perm[s] += 1

        for i in range(len(s2)-len(s1)+1):
            count = defaultdict(int)
            for s in s2[i:i + len(s1)]:
                if s not in perm:
                    break
                if count[s] >= perm[s]:
                    break
                else:
                    count[s] += 1
            if count == perm:
                return True
        return False
