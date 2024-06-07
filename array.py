def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
arr = [9, 8, 7, 6, 5, 4, 3,2,1]

bubble_sort(arr)
print( arr)

def bubble_sort2(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[44,55,55,66,22,11,1]

bubble_sort2(arr)
print(arr)