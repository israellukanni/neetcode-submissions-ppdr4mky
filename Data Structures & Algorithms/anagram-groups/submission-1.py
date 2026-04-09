class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #need a way to check if items in list have the same letters in the same amounts
        # first idea that comes to mind is sorting each word
        # strs = ["act","pots","tops","cat","stop","hat"]
        #results = [] #[[act,cat],[pots,tops,stop],[hat]]
        newdict = {} # {act:0,opst:1,aht:2 }
        for word in strs:
            sortword = "".join(sorted(word))
            if sortword in newdict.keys():
                newdict[sortword].append(word)
            else:
                newdict[sortword] = [word]
                #results.append([word])
        return list(newdict.values())
