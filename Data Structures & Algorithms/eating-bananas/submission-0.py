class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #we need helper function here
        def can_finish(k):
            hours=0
            for p in piles:
                #here use ceiling division to calculate hours for this pile
                hours += (p+k-1)//k
            return hours <= h
        
        left,right = 1 , max(piles)

        res = right
        while left <= right:
            mid = left + (right -left) //2

            if can_finish(mid):
                res = mid #this speed work but we will try mor to get speed more slower
                right = mid-1
            else:
                left = mid +1#too slow
        return res
