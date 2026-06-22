class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #two pointers
        n = len(nums)
        hashmap={0:1}
        count=0
        prefixSum=0
        for num in nums:
            prefixSum += num
            #if prefixSum-k exists in hashmap, it means we found a subarray
            if (prefixSum-k) in hashmap:
                count+= hashmap[prefixSum-k]
            #update map with current prefix sum
            hashmap[prefixSum]= hashmap.get(prefixSum,0)+1

        return count 
            

