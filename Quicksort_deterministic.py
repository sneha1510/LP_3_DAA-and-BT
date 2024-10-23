#deterministic quicksor
def quicksort(arr):
    if len(arr)<=1:
        return arr
    p=arr[len(arr)//2]
    left=[x for x in arr if x<p]
    middle=[x for x in arr if x==p]
    right=[x for x in arr if x>p]
    return quicksort(left)+middle+quicksort(right)

arr=[10, 7, 8, 9,1, 5, 89]
print("Usorted array",arr)
sorted_arr=quicksort(arr)
print("sorted array",sorted_arr)