def sumOfPair(x,total):
    for i in range(len(x)):
        for j in range(len(x)):
            sum = x[i]+x[j]
            if sum == total:
                return {x[i],x[j]}



def sortingOFarray(arr):
    for x in range(len(arr)):
        temp = arr[x]
        for y in range(len(arr)):
            if arr[x] < arr[y]:
                arr[x],arr[y] = arr[y],arr[x]
                print(arr)
    print(arr)
if __name__ == '__main__':
    sum = sumOfPair([11, 15, 6, 8, 9, 10],16)
    sortingOFarray([11, 15, 6, 8, 9, 10])
    print(sum)
