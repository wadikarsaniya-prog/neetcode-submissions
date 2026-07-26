class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in range(len(strs)):
            key = sorted(strs[i])
            key = "".join(sorted(strs[i]))
            if key in d:
                d[key].append(strs[i])
            else:
                d[key]=[]
                d[key].append(strs[i])

        return list(d.values())
