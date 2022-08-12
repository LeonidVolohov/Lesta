"""
Одним из самых быстрых алгоритмов сортировки является Timsort, который
был изобретен в 2002 году. И данный алгоритм является стандартным алгоритмом
сортировки в Python.

Timsort не является самостоятельным алгоритмом сортировки, а является гибридом
комбинации нескольких других алгоритмов.

Основная суть алгоритма заключается в следующем:
 - входной массив разделяется на подмассивы
 - каждый массив сортируется обычной сортировкой вставками
 - отсортированные подмассивы собираются в единый массив с помощью
   сортировки слиянием
"""
from random import randint


MIN_MERGE = 32

def get_minimum(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
 
def merge(array, l, m, r):
    first_length, second_length = m - l + 1, r - m
    left, right = [], []
    for i in range(0, first_length):
        left.append(array[l + i])
    for i in range(0, second_length):
        right.append(array[m + 1 + i])
 
    i, j, k = 0, 0, l

    while i < first_length and j < second_length:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < first_length:
        array[k] = left[i]
        k += 1
        i += 1

    while j < second_length:
        array[k] = right[j]
        k += 1
        j += 1

def timSort(array):
    n = len(array)
    minRun = get_minimum(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion_sort(array, start, end)

    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(array, left, mid, right)
        size = 2 * size


def main():
    min_length = 15
    max_length = 30
    length = randint(min_length, max_length)

    array = []
    for i in range(length):
        random_int = randint(-1000, 1000)
        array.append(random_int)
    print(array)
    timSort(array)
    print(array)

if __name__ == "__main__":
    main()
