class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        n= len(arr)
        for i in range (n-1,-1,-1):
            num = arr[i]
            arr[i]=greatest
            if num>greatest:
                greatest = num
        return arr
                
        