class MergeSortedArrays:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def merge(self):
        n = len(self.arr1)
        m = len(self.arr2)
        
        i = n - 1
        j = 0
        
        while i >= 0 and j < m:
            if self.arr1[i] > self.arr2[j]:
                self.arr1[i], self.arr2[j] = self.arr2[j], self.arr1[i]
            
            i -= 1
            j += 1
        
        self.arr1.sort()
        self.arr2.sort()

    def display(self):
        print("Modified arr1:", self.arr1)
        print("Modified arr2:", self.arr2)

arr1 = [1, 5, 9]
arr2 = [2, 6, 8, 10]

merger = MergeSortedArrays(arr1, arr2)
merger.merge()
merger.display()
