class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        smallest_s=strs[0]
        for s in strs:
            if len(s)< len(smallest_s):
                smallest_s=s
        prefix=smallest_s
        for s in strs:
            cur_prefix=""
            for i in range(len(smallest_s)):
                if s[i] != smallest_s[i]:
                    break
                else:
                    cur_prefix+=s[i]
            if len(cur_prefix) < len(prefix):
                prefix=cur_prefix
        return prefix
            




