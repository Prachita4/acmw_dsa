class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def rotate_90_degrees_clockwise(self):
        n = len(self.matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[n - j - 1][i]
                self.matrix[n - j - 1][i] = self.matrix[n - i - 1][n - j - 1]
                self.matrix[n - i - 1][n - j - 1] = self.matrix[j][n - i - 1]
                self.matrix[j][n - i - 1] = temp
    
    def display(self):
        for row in self.matrix:
            print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m = Matrix(matrix)
m.rotate_90_degrees_clockwise()
m.display()
