class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsize=float("inf")
        left=0
        curr_sum=0
        for right in range(len(nums)):

            curr_sum+=nums[right]
            if curr_sum >= target:
                
                #shrink from left
                while left<=right and curr_sum >=target:
                    minsize = min(minsize, right-left+1)
                    curr_sum -= nums[left]
                    left+=1

        return minsize if minsize!=float("inf") else 0
            