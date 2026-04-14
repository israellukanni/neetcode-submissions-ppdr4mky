class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
        for s in strs: 
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded = []
        i = 0 
        while i < len(s): #   4#neet4#code
            
            length = s[i]
            i += 1
            while i <len(s) and s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            word = s[i+1 : i+1+length]
            decoded.append(word)
            i += 1 +length
        return decoded
            
