def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 

number  = [42, 19, 33, 8, 55] 
bubble_sort_descending(number) 
print("Daftar angka yang diurutkan secara terbalik :")
for nilai in number:
    print(nilai)