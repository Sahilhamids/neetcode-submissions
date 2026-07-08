class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        def can_ship(cap):
            total_days = 1
            curr_load=0
            for w in weights:

                if curr_load+w > cap:
                    curr_load = w
                    total_days+=1
                else:
                    curr_load += w
            return total_days <= days
        low = max(weights)
        high = sum(weights)

        result = high

        while low<=high:

            mid = low + (high-low)//2
            if can_ship(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result

