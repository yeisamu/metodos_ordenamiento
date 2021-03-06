# -*- coding: utf-8 -*-

# *************************** Inserción Directa **********************
def insercionDirecta(lista, tam):
    for i in range(1, tam):
        v = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > v:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = v

# *************************** HeapSort **********************
def heapsort(lista, tam):
    for k in range(tam - 1, -1, -1):
        for i in range(0, k):
            item = lista[i]
            j = (i + 1) / 2
            while j >= 0 and lista[j] < item:
                lista[i] = lista[j]
                i = j
                j = j / 2
            lista[i] = item
        temp = lista[0]
    lista[0] = lista[k]
    lista[k] = temp

# *************************** Quick Sort **********************
def quicksort(lista, izq, der):
    i = izq
    j = der
    x = lista[(izq + der) / 2]

    while (i <= j):
        while lista[i] < x and j <= der:
            i = i + 1
        while x < lista[j] and j > izq:
            j = j - 1
        if i <= j:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            i = i + 1
            j = j - 1

        if izq < j:
            quicksort(lista, izq, j)
    if i < der:
        quicksort(lista, i, der)

# *************************** Merge Sort **********************
def merge_sort(numbers):
    """Punto de entrada del algoritmo"""
    n = len(numbers)
    if (n == 1): return numbers

    left = merge_sort(numbers[:(n / 2)])
    right = merge_sort(numbers[(n / 2):])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    len_left = len(left)
    len_right = len(right)

    while (i < len_left or j < len_right):
        if (i >= len_left):
            result.append(right[j])
            j = j + 1
        elif (j >= len_right):
            result.append(left[i])
            i = i + 1
        elif (left[i] < right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    return result

# *************************** Ordenamiento por Conteo **********************
def counting_sort(array, maxval):
    n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array

# *************************** Radix Sort **********************
def radix_sort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in random_list:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_random_list:
            return new_list[0]

        random_list = []
        rd_list_append = random_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)