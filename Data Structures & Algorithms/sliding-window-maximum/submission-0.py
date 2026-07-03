from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0:
            return []
        
        dq = deque()
        res = []
        for i , num in enumerate(nums):
            #remove smaller elements from back
            #as they can never be max
            
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)

            #remove front if outside current window
            if dq[0] <= i - k:
                dq.popleft()
          #add max to result when window is full
            if i>= k-1:
                res.append(nums[dq[0]])
        return res 
