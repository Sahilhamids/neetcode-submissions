
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #here we need to slide the window variable size window and check if the new character comming is repeated in the hashmap
        # if repeated we will shrink the window from left if not repeated expand from right 
        n = len(s)
        if n==0:
            return 0
        freq={}
        max_len=0
        l,r=0,0
        while l<=r and r<n:

            if s[r] in freq and freq[s[r]]>=l:
                     
                l = freq[s[r]] + 1
            
            freq[s[r]]=r
            
            max_len = max(max_len, r-l+1)
            r += 1

        return max_len


