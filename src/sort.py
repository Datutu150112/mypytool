def bubble_sort(arr, reverse = False):
    if reverse:
        l = len(arr)
        for i in range(l):
          for j in range(l - i - 1):
            if arr[j] < arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
        return arr
    else:
        l = len(arr)
        for i in range(l):
            for j in range(0,l-i-1):
                if arr[j] > arr[j+1]:
                    t = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = t
        return arr

def bucket_sort(arr, reverse = False):
    # breakpoint()
    m_max = arr[0]
    arr1 = []
    out = []
    mem = -1
    for i in arr:
        if(i > m_max):
            m_max = i
    for i in range(m_max + 1):
        arr1.append(0)
    for i in arr:
        arr1[i] += 1
    if reverse:
        for i in range(len(arr1)):
            ins = len(arr1) - i - 1
            for j in range(arr1[ins]):
                out.append(ins)
        return out
    else:
        for i in arr1:
            mem += 1
            if i != 0:
                for j in range(i):
                    out.append(mem)
        return out

def selection_sort(arr, reverse = False):
    if reverse:
        for i in range(len(arr) - 1):
            m_min = arr[i]
            m_min_i = 0
            for j in range(i,len(arr)):
                if(arr[j] >= m_min):
                    m_min = arr[j]
                    m_min_i = j
            arr[i] , arr[m_min_i] = arr[m_min_i] , arr[i]
        return arr
    else:
        for i in range(len(arr) - 1):
            m_min = arr[i]
            m_min_i = 0
            for j in range(i,len(arr)):
                if(arr[j] <= m_min):
                    m_min = arr[j]
                    m_min_i = j
            arr[i] , arr[m_min_i] = arr[m_min_i] , arr[i]
        return arr

def insertion_sort(arr, reverse = False):
    if reverse:
        n = len(arr)
        for i in range(1,n):
            k = arr[i]
            j = i - 1
            while j >= 0 and k > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = k
        return arr
    else:
        n = len(arr)
        for i in range(1,n):
            k = arr[i]
            j = i - 1
            while j >= 0 and k < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = k
        return arr

def shell_sort(arr, reverse = False):
    if reverse:
        n = len(arr)
        len_t = n // 2
        while len_t > 0:
            for i in range(len_t, n):
                temp = arr[i]
                j = i
                while j >= len_t and arr[j - len_t] < temp:
                    arr[j] = arr[j - len_t]
                    j -= len_t
                arr[j] = temp
            len_t //= 2
        return arr
    else:
        n = len(arr)
        len_t = n // 2
        while len_t > 0:
            for i in range(len_t, n):
                temp = arr[i]
                j = i
                while j >= len_t and arr[j - len_t] > temp:
                    arr[j] = arr[j - len_t]
                    j -= len_t
                arr[j] = temp
            len_t //= 2
        return arr

def merge_sort(arr, reverse = False):
    out = merge_sortt(arr)
    if reverse:
        return out.reverse()
    else:
        return out

def merge_sortt(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sortt(arr[:mid])
    right_half = merge_sortt(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

def quick_sort(arr, reverse = False):
    if len(arr) <= 1:
        return arr
    right = len(arr)
    std = arr[0]
    leftl = []
    rightl = []
    time = 0
    for i in arr:
        if time == 0:
            time += 1
            continue
        if i <= std:
            leftl.append(i)
        if i > std:
            rightl.append(i)
        time += 1
    if reverse:
        return quick_sort(rightl,True) + [std] + quick_sort(leftl,True)
    else:
        return quick_sort(leftl) + [std] + quick_sort(rightl)

def ascending_order(arr, sorting_algorithm):
    out = sorting_algorithm(arr)
    return out

def descending_order(arr, sorting_algorithm):
    out = sorting_algorithm(arr,True)
    return out

def sort(arr, sorting_algorithm = quick_sort, sort_order = ascending_order, reverse = None):
    if reverse != None:
        return sorting_algorithm(arr,reverse)
    out = sort_order(arr, sorting_algorithm)
    return out