class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res=0
        maxf = 0 #tracks most frequent element in surrent substring
        left = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right],0)+1
            maxf = max(maxf, count[s[right]])

            #if current window size minus most frequent char count>k shrink from left
            if (right-left+1)-maxf > k:
                count[s[left]]-=1
                left+=1
            res = max(res, right-left+1)
        return res