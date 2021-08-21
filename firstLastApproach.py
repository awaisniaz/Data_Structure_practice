def swapFirst(arr,n):
    i = 0
    j = n

    while i != j:
        print(i)
        print(j)
        arr[i],arr[j] = arr[j],arr[i]
        i = i+1

    print(arr)
    pass

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    n = len(arr)-1
    swapFirst(arr,n)