import math

def pascal_element(r, c):
    return math.comb(r, c)

def pascal_row(n):
    return [math.comb(n, i) for i in range(n + 1)]

def pascal_triangle(n):
    return [[math.comb(i, j) for j in range(i + 1)] for i in range(n)]

def main():
    print("Select an option:")
    print("1. Find the element at position (r, c)")
    print("2. Print the nth row of Pascal's triangle")
    print("3. Print the first n rows of Pascal's triangle")
    option = int(input())

    if option == 1:
        r = int(input("Enter the row number r: "))
        c = int(input("Enter the column number c: "))
        print("Element at position (r, c):", pascal_element(r, c))

    elif option == 2:
        n = int(input("Enter the row number n: "))
        print(f"The {n}-th row of Pascal's triangle:", pascal_row(n))

    elif option == 3:
        n = int(input("Enter the number of rows n: "))
        print("First", n, "rows of Pascal's triangle:")
        triangle = pascal_triangle(n)
        for row in triangle:
            print(row)

main()
