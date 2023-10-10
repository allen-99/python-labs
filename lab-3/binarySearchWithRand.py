import random

array = random.sample(range(100), 100)
array.sort()

def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

x = int(input('Введите число для поиска от 0 до 99: '))
result = binarySearch(array, 0, len(array), x)
print("Индекс числа ", result)
