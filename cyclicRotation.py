def cyclicRotation(arr,n,d):
    for i in range(d):
        temp = arr[len(arr)-1]
        for j in range(len(arr)-1,0,-1):
            arr[j] = arr[j-1]
        arr[0] = temp

        print(arr)
if __name__ == '__main__':

    arr = [1,2,3,4,5]
    n = len(arr)
    d = 2
    cyclicRotation(arr,n,d)