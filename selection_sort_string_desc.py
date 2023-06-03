def selection_sort(arr):
    n = len(arr)
    for i in range (n-1) :
        min_index = i
        for j in range (n-i-1):
            if arr[j] > arr[min_index]:
                min_index = j
                arr[j],arr[min_index] = arr[min_index], arr[j]

arr = ["z","b","a","f","c"]
selection_sort(arr)
print(" Hasil pengurutan : ",arr)