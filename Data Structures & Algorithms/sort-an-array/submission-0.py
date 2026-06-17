class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: handle empty or single-element lists
        if len(nums) <= 1:
            return nums
        
        # Divide
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Conquer: Create a NEW list for the merged result
        merged = []
        p1, p2 = 0, 0

        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                merged.append(left[p1])
                p1 += 1
            else:
                merged.append(right[p2])
                p2 += 1
        
        # Append remaining elements
        merged.extend(left[p1:])
        merged.extend(right[p2:])
        
        return merged