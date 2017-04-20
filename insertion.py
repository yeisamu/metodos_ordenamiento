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
def swap(lista,i, j):
	lista[i], lista[j] = lista[j], lista[i]

def heapify(lista,end,i):
    l=2 * i + 1
    r=2 * (i + 1)
    max=i
    if l < end and lista[i] < lista[l]:
        max = l
    if r < end and lista[max] < lista[r]:
        max = r
    if max != i:
        swap(lista,i, max)
        heapify(lista,end, max)

def heap_sort(lista):
    end = len(lista)
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):
        heapify(lista,end, i)
    for i in range(end-1, 0, -1):
        swap(lista,i, 0)
        heapify(lista,i, 0)
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
def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break

	return result

def mergesort(list):
	if len(list) < 2:
		return list

	middle = len(list)/2
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])

	return merge(left, right)

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