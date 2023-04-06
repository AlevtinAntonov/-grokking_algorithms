



def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1,2,3,10]))

def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])

print(sum_array([1,2,3,10]))
array1 = [1, 12, 2, 5, 3,10]
def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

print(count(array1))

def max_number(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_number(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max_number(array1))





from time import sleep
def print_items2(list):
    for item in list:
        sleep(1)
        print(item)

print_items2([1,1,1,1,1,1])



