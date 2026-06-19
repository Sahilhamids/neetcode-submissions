class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left product and right product method
        left_product=[1]
        n=len(nums)
        for i in range(1,n):
            left_product.append(left_product[i-1]*nums[i-1])
        
        #final product except self 
        running=1
        
        for i in range(n-2,-1,-1):
            
            running*= nums[i+1]
            left_product[i]*=running
        return left_product


        