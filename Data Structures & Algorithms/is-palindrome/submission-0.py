class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.strip()
        j=len(s)-1
        i=0
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i]!=s[j]:
                return False
            j-=1
            i+=1
        
        return True
        



        