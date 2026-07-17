import random

class RandomizedSet:

    def __init__(self):
        self.vals = []          # array of values
        self.idx_map = {}       # value -> index in self.vals

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False

        # index of the value we want to remove
        idx_to_remove = self.idx_map[val]
        last_val = self.vals[-1]

        # move the last element into the removed slot
        self.vals[idx_to_remove] = last_val
        self.idx_map[last_val] = idx_to_remove

        # remove the last slot (which now duplicates last_val)
        self.vals.pop()
        del self.idx_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()