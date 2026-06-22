from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1,c2,count1,count2=0,0,0,0

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
        count1=0
        count2=0
        n=len(nums)
        for num in nums:
            if num==c1:
                count1+=1
            elif num==c2:
                count2+=1
        if count1 > n//3:
            res.append(c1)
        if count2 > n//3:
            res.append(c2)
        return res