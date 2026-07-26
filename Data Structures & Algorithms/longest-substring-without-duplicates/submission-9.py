class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i=0
        j=i+1
        
        if s == "":
            return 0

        if len(s)==1:
            return 1

        subs = set()
        subs.add(s[0])

        while j<len(s):

            while s[j] in subs:
                subs.remove(s[i])
                i+=1

            subs.add(s[j])
            j+=1
            
            longest = max(longest, j-i)

        return longest
