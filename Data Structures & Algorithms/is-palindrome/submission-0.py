class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        l,r=0,n-1

        while l<r:
            if not s[l].isalnum() or not s[r].isalnum():
                if not s[l].isalnum():
                    l+=1
                if not s[r].isalnum():
                    r-=1
                
            elif s[l].lower() != s[r].lower():
                return False
            else:
                r-=1
                l+=1

        return True
        