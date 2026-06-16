class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) !=  len(s):
            return False
        #fix array of 26 lowercase english letters
        count=[0]*26
        
        for i in range(len(s)):

            count[ord(s[i]) - ord('a')] +=1
            count[ord(t[i]) - ord('a')] -=1
        
        # if anagram all balences must be zero
        for val in count:
            if val != 0:
                return False
        return True