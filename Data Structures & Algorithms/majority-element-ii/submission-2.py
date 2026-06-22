from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1,c2,count1,count2=0,0,0,0
        n=len(nums)
        for num in nums:
            if num==c1:
                count1+=1
            elif num==c2:
                count2+=1

            elif count1==0:
                c1=num
                count1=1
            elif count2==0:
                c2=num
                count2=1
            else:
                count1-=1
                count2-=1
        res=[]
        # Phase 2: Verification
        res = []
        for cand in [c1, c2]:
            # Use 'if cand is not None' to handle empty/short array cases
            # Use 'if cand not in res' to ensure uniqueness
            if cand is not None and cand not in res and nums.count(cand) > n // 3:
                res.append(cand)
        return res