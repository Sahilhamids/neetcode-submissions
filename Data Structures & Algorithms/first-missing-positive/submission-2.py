class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        
        # Rearrange elements to to position as nums[i] should be at position index nums[i]-1
        # Using elements as key 
        for i in range(n):

            #olny swap when the number is in range 1 to n and is not already in correct position
            while 1<=nums[i]<=n and nums[nums[i]-1] != nums[i]:
                val = nums[i]    
                nums[i],nums[val-1]=nums[val-1],nums[i]
                
        # 2nd pass to check if position is correct 
        for i in range(n):
        
            if nums[i] == i+1:
                continue
            else:
                #element missing and the index at which correct element is missing is the answer
                return int(i+1)
        return n+1