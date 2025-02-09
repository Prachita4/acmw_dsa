class FindDuplicateAndMissing:
    def __init__(self, nums):
        self.nums = nums

    def find_missing_and_duplicate(self):
        n = len(self.nums)
        sum_of_elements = 0
        sum_of_squares = 0
        for num in self.nums:
            sum_of_elements += num
            sum_of_squares += num * num
        
        expected_sum = n * (n + 1) // 2
        expected_sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6

        sum_diff = expected_sum - sum_of_elements
        square_sum_diff = expected_sum_of_squares - sum_of_squares

        missing_plus_duplicate = square_sum_diff // sum_diff
        duplicate = (missing_plus_duplicate - sum_diff) // 2
        missing = missing_plus_duplicate - duplicate

        return duplicate, missing

    def display(self):
        duplicate, missing = self.find_missing_and_duplicate()
        print(f"Duplicate: {duplicate}, Missing: {missing}")


nums = [1, 2, 2, 4, 5]
finder = FindDuplicateAndMissing(nums)
finder.display()
