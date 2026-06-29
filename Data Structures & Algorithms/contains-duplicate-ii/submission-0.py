class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        if n==1:
            return False
        hmap = {}
        for i, num in enumerate(nums):
            if num in hmap and i-hmap[num] <= k:
                return True
            hmap[num]=i
        return False
        