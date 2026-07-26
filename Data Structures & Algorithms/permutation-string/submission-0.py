class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for alph in s1:
            if alph in need:
                need[alph]+=1
            else:
                need[alph]=1

        j=0
        have = {}
        for alph in range(len(s1)):
            if s2[alph] in have:
                have[s2[alph]]+=1
            else:
                have[s2[alph]]=1

        for i in range(len(s1),len(s2)):

            if need==have:
                return True

            if s2[i] in have:
                have[s2[i]]+=1
            else:
                have[s2[i]]=1

            have[s2[j]] -= 1
            if have[s2[j]] == 0:
                del have[s2[j]]

            j+=1

        if need == have:
            return True
        else: return False
            