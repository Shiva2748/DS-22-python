def fun(arr):
    prod = 1
    for i in range(len(arr)):
        prod = prod*arr[i]

    for i in range(len(arr)):
        arr[i] = prod//arr[i]
    return arr


arr = list(map(int,input().split()))
print(fun(arr))
