def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, 9))
print(binary_search(my_list, 6))
print(binary_search(my_list, 1))

def binary_search_2(arr, target):
    if not arr:
        return -1

    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search_2(arr[:mid], target)
    else:
        return binary_search_2(arr[mid+1:], target)


print(binary_search_2([6, 7, 8, 9, 10], 7))
print(binary_search_2([6, 7, 8, 9, 10], 100))