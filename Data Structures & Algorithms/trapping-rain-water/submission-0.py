class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        
        left,right=0,n-1
        leftmax=height[left]
        rightmax=height[right]
        water=0
        while left < right:
            #always move the pointer pointing to smaller max height
            if leftmax < rightmax:
                left+=1
                leftmax=max(height[left],leftmax)
                water+= max(0,leftmax-height[left])
            else:
                right-=1
                rightmax = max ( rightmax, height[right])
                water+= max(0, rightmax-height[right])
        return water


        