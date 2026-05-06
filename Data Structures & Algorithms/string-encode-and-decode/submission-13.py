class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            final += "+" + str(len(s))+ "+" + s
        return final
    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        i = 0 
        while i < len(s):
            if s[i] == "+":
                i += 1
                length = ""
                while s[i] != "+":
                    length += s[i]
                    i += 1
                length = int(length)

                decoded.append(s[i+1:i+1+length])
                i += 1 + length
            # else:
            #     i += 1
        return decoded