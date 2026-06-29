class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights)<2:
            return 0
        n= len(heights)
        left=0
        right=n-1
        max_water=0
        while left<right:
            h=min(heights[left],heights[right])
            w=right-left

            max_water= max(max_water,h*w)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water




        