class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = Counter(t)
        missing = len(t)

        left = 0
        best_start = 0
        best_len = float('inf')
        
        
        for right,char in enumerate(s):
            
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            while missing == 0:
                window_len = right - left + 1

                if window_len < best_len:
                    best_start = left
                    best_len = window_len
                
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]
