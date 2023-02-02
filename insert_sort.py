def func(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

if __name__ == '__main__':
    a = [222,8473,543,3422,2323,4575,3532]
    print(func(a))
