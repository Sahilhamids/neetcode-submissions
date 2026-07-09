class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(target_max):
            subarrays = 1
            curr_sum = 0
            for n in nums:
                curr_sum += n
                if curr_sum > target_max:
                    subarrays += 1
                    curr_sum = n
            return subarrays <= k
        
        left, right = max(nums) , sum(nums)

        while left <= right:

            mid = (left+right) //2
            if can_split(mid):
                res = mid 
                right = mid - 1
            else:
                left = mid + 1
        return res
        