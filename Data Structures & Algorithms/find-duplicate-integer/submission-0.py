class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        slow =0
        fast =0
        #find cillision
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #FIND DUPLICATE
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

        