from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)

        for num in nums:
            hashmap[num]+=1
        majority=nums[0]
        max=0
        for num in hashmap:
            
            if hashmap[num] > (len(nums)/2):
                return num


