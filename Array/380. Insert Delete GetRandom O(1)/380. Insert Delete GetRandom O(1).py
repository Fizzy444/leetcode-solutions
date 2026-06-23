import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.pos = {}
    def insert(self, val):
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True
    def remove(self, val):
        if val not in self.pos:
            return False
        ind = self.pos[val]
        last = self.nums[-1]
        self.nums[ind] = last
        self.pos[last] = ind
        self.nums.pop()
        del self.pos[val]
        return True
    def getRandom(self):
        return random.choice(self.nums)