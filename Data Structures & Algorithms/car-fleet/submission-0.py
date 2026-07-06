class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, speed) and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for p, s in cars:
            # Time to reach target
            time = (target - p) / s
            
            # If stack is empty or current car takes longer than the 
            # car ahead (top of stack), it forms a new fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
            
            # If time <= stack[-1], it joins the fleet ahead, 
            # so we don't need to add it to the stack.
            
        return len(stack)