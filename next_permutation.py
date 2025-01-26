def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return arr

def main():
    n = int(input("Enter number of elements in the array: "))
    arr = []
    
    print("Enter array elements:")
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    
    result = next_permutation(arr)
    
    print("Next permutation:", result)

main()
