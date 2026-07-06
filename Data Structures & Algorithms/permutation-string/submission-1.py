class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        s1_freq = [0]*26
        window_freq = [0]*26

        for i in range(len(s1)):
            s1_freq[ord(s1[i])-ord("a")] +=1
            window_freq[ord(s2[i])-ord("a")]+=1
                    
        for i in range(len(s2)-len(s1)):
            if s1_freq == window_freq:
                return True
            window_freq[ord(s2[i])-ord("a")]-=1
            window_freq[ord(s2[i+len(s1)])-ord('a')]+=1
        return s1_freq == window_freq

        

        



