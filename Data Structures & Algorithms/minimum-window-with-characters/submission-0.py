from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)

        if n<m:
            return ""
        countT={}
        for c in t:
            countT[c] = countT.get(c,0) +1
        have,need=0,len(countT)
        res,resLen=[-1,-1],float("inf")
        window={}
        l=0
        for r in range(n):
            char = s[r]
            window[char]= window.get(char,0) + 1
            if char in countT and window[char] == countT[char]:
                have+=1
            
            while have==need:
                if (r-l+1 )< resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                #pop from the left
                window[s[l]] -=1
                if s[l] in countT and window[s[l]]  < countT[s[l]]:
                    have -= 1
                l+=1
        l,r=res
        return s[l:r+1] if resLen != float("inf") else ""