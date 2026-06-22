from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap=defaultdict(int)
        res=set()
        n=len(nums)
        for num in nums:
            hashmap[num]+=1
            if hashmap[num] > n//3:
                res.add(num)
        return list(res)
            