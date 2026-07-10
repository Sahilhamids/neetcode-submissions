class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # 1. Find the peak
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        
        # 2. Search in left (increasing)
        res = self.binarySearch(mountainArr, target, 0, peak, True)
        if res != -1:
            return res
            
        # 3. Search in right (decreasing)
        return self.binarySearch(mountainArr, target, peak + 1, n - 1, False)

    def binarySearch(self, mountainArr, target, left, right, is_increasing):
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            
            if is_increasing:
                if val < target: left = mid + 1
                else: right = mid - 1
            else:
                if val > target: left = mid + 1
                else: right = mid - 1
        return -1