def selection_sort(arr):
    n = len(arr)
    for i in range (n-1) :
        min_index = i
        for j in range (n-i-1):
            if arr[j][0] < arr[j+1][0]:
                min_index = j
                arr[i],arr[min_index] = arr[min_index], arr[i]

arr = [[3,5],[1,2],[4,6],[2,1]]
selection_sort(arr)
print(" Hasil pengurutan : ",arr)