# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        # taking a list, iterating through
        # take the element compare to the prev, if >= then keep it where it is
        # otherwise compare to the next prev (if any) and then eventually swap
        Lpairs = []
        
        for i in range(len(pairs)):
            curr = pairs[i]
            j = 0
            while j < i:
                if curr.key < pairs[j].key:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                j += 1
            Lpairs.append(pairs[:])
        return Lpairs
            
