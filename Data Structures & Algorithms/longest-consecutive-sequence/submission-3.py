class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet=set()
        for num in nums:
            hashSet.add(num)
        ans=1

        for num in nums:
            
            if num-1 in hashSet:
                continue
            curr=1
            while num+1 in hashSet:
                curr+=1
                num+=1
                ans= max(ans,curr)
        return ans

        