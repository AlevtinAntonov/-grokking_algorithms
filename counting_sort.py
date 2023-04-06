# Сортировка подсчетами (Counting Sort) - это алгоритм сортировки, который использует подсчет количества каждого элемента в массиве и сортировку по вспомогательному массиву.
#
# Отсортируйте массив целых не отрицательных чисел.
# Гарантируется, что минимальный элемент равен 0. Максимальный элемент может меняться.

import time
import random
from quick_sort import quick_sort

m = 100000000
n = 1000000

nums = [random.randint(0, m) for _ in range(n)]


def countig_sort(arr):
    count = [0] * (max(arr) + 1)
    for i in arr:
        count[i] += 1
    result = []
    for i, c in enumerate(count):
        result += [i] * c
    return result


start = time.time()
countig_sort(nums)
end = time.time()
print('counting_sort ', end - start)

start2 = time.time()
quick_sort(nums)
end2 = time.time()
print('quick_sort  ', end2 - start2)
