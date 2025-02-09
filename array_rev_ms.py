class CountInversions:
    def __init__(self, arr):
        self.arr = arr
        self.inv_count = 0

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            self.merge(arr, left, right)

    def merge(self, arr, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                self.inv_count += len(left) - i
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def count_inversions(self):
        self.merge_sort(self.arr)
        return self.inv_count

    def display(self):
        print("Number of inversions:", self.count_inversions())

arr = [1, 20, 6, 4, 5]
inverter = CountInversions(arr)
inverter.display()
