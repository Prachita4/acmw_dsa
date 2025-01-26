def largest_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def main():
    n = int(input("Enter number of elements in the array: "))
    arr = []
    
    print("Enter array elements:")
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    
    result = largest_sum(arr)
    
    print("Largest sum of a subarray is:", result)

main()
