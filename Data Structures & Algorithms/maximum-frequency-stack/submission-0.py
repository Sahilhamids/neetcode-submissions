from collections import defaultdict
class FreqStack:

    def __init__(self):
        # Map elements to its current freq
        self.freq_map = defaultdict(int)
        #maps freq to a stack of elements at that freq
        self.group_map = defaultdict(list)
        #tracks maximum freq so far
        self.max_freq=0
    def push(self, val: int) -> None:
        f = self.freq_map[val] + 1
        self.freq_map[val] = f
        
        #update max freq found so far\
        if f > self.max_freq:
            self.max_freq = f
        # add the value to the stack at the freq f
        self.group_map[f].append(val)
    def pop(self) -> int:
        val = self.group_map[self.max_freq].pop()
        # decrement its freq
        self.freq_map[val]-=1
        # if stack for maxfreq does not exist decrement maxfreq by one
        if not self.group_map[self.max_freq]:
            self.max_freq -= 1
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()