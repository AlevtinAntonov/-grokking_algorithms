arr = [5, 13, 8, 46, 0, -5, 7, 2]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]


print(arr)