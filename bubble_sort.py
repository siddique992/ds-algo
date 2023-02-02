def func(arr):
    l = len(arr)
    while True:
        s = True
        for i in range(l):
            if (i + 1) < l and arr[i] < arr[i+1]:
                s = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if s == True:
            break
    return arr

if __name__ == '__main__':
    a = arr = [222,8473,543,3422,2323,4575,3532]
    print(func(a))
