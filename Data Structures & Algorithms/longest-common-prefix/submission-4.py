class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        first= strs[0]

        for i in range(len(first)):
            char= first[i]
            for s in strs:
                if i==len(s) or s[i] != char:
                    return first[:i]
        return first




