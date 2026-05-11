class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            final += str(len(s)) + "#" + s
        return final

    def decode(self, s: str) -> List[str]:
        # print()
        decoded = []
        i = 0 
        while i < len(s):
            # length = ""
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            # print(s,s[i:j])
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1+ length
        return decoded