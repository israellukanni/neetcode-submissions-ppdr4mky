class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" +s
        return encoded


    def decode(self, s: str) -> List[str]:

        decoded = []

        i = 0
        while i < len(s):
            num = ""
            while i < len(s) and s[i] != "#":
                num += s[i]
                i += 1
                # print(num)
            decoded.append(s[i+1:i+1+int(num)])
            i += int(num) + 1
        
        return decoded