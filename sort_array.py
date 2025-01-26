def sort_array(arr):
    low=0
    mid=0
    high=len(arr)-1
    while low<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        else if mid==1:
            mid+=1
        else:
            arr[high],arr[mid]=arr[mid],arr[high]
            high-=1
    return arr

def main():
    n = int(input("Enter number of elements in the array: "))
    arr = []
    
    print("Enter array elements (only 0, 1, 2):")
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    
    sorted_array = sort_array(arr)
    
    print("Sorted array:", sorted_array)

main()
