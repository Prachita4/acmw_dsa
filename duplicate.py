class DuplicateFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_duplicate(self):
        slow = self.nums[0]
        fast = self.nums[0]

        while True:
            slow = self.nums[slow]
            fast = self.nums[self.nums[fast]]
            if slow == fast:
                break

        slow = self.nums[0]
        while slow != fast:
            slow = self.nums[slow]
            fast = self.nums[fast]

        return slow

    def display(self):
        print(self.find_duplicate())

nums = [3, 1, 3, 4, 2]
finder = DuplicateFinder(nums)
finder.display()
