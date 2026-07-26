class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        need = {}

        for char in t:
            if char in need:
                need[char]+=1
            else:
                need[char]=1
            
        left = 0
        formed = 0
        req = len(need)
        smallest_count = float('inf')
        start = left

        for right in range(len(s)):
            if s[right] in have:
                have[s[right]]+=1
            else:
                have[s[right]]=1

            if s[right] in need and have[s[right]]==need[s[right]]:
                formed+=1

            while formed == req:

                if right-left+1 < smallest_count:
                    smallest_count = right-left+1
                    start = left 
                
                have[s[left]]-=1
                if s[left] in need and have[s[left]]<need[s[left]]:
                    formed-=1

                left+=1

        if smallest_count == float('inf'):
            return ""

        return s[start : start + smallest_count]




            











