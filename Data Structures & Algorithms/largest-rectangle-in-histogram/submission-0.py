class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0]+ heights + [0]
        max_area=0
        for i,h in enumerate(heights):

            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                area = height * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area
        