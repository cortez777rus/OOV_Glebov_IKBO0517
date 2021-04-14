def funct(arr, a=0, res=0):
    if a >= len(arr):
        return res
    else:
        res = funct(arr, a+1, res +arr[a])
    return res
arr = [1,2,3,4,5,6,7,8]
print(funct(arr))