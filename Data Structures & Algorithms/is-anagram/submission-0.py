class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) !=  len(s):
            return False
        hashmap={}
        for i in range(len(t)):
            if t[i] not in hashmap:
                hashmap[t[i]]=1
            else:
                hashmap[t[i]] +=1
        
        for c in s:
            if c not in hashmap:
                return False
            elif c in hashmap:
                if hashmap[c]==0:
                    return False
                else:
                    hashmap[c]-=1
        return True