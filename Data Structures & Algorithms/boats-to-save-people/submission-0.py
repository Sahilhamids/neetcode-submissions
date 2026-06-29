class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # If the lightest and heaviest can fit together
            if people[left] + people[right] <= limit:
                left += 1
            
            # The heaviest always gets a boat (either alone or with the lightest)
            right -= 1
            boats += 1
            
        return boats