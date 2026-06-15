class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k= k % n
        # Step 1: reverse full array
        left,right=0,n-1
        while left<right:
            nums[left],nums[right]= nums[right], nums[left]
            left+=1
            right-=1
        #step 2: reverse first k elements
        left, right= 0,k-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        #step 3: reverse remaining elements
        left,right= k,n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums