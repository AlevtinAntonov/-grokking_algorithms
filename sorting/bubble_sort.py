def bubble_sort(list_1):
    for i in range(len(list_1) - 1):
        for j in range(len(list_1) - 1):
            if list_1[j] > list_1[j + 1]:
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
    return list_1


list1 = [5, 13, 8, 46, 0, -5, 7, 2]
list2 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь']

print("The unsorted list is: ", list1)
print("The sorted list is: ", bubble_sort(list1))

print("The unsorted list is: ", list2)
print("The sorted list is: ", bubble_sort(list2))


nums = [4, 1, 6, 3, 2, 7, 8]
n = 1
while n < len(nums):
   for i in range(len(nums) - n):
       if nums[i] > nums[i + 1]:
           nums[i], nums[i + 1] = nums[i + 1], nums[i]
   n += 1

print(nums)