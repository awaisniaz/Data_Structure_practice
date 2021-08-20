class ArrayRotation:
    def oneByOneRotation(self,arr,d):
        for i in range(d):
            print(i)
            temp = arr[0]
            for j in range(len(arr)-1):
                arr[j] = arr[j+1]
            arr[len(arr)-1] = temp
        print(arr)

    # def jugglingRotation(self,arr,d,n):
    #     d = d % n
    #     g_c_d = rotation.gcd(d, n)
    #     for i in range(g_c_d):
    #
    #         # move i-th values of blocks
    #         temp = arr[i]
    #         j = i
    #         while 1:
    #             k = j + d
    #             if k >= n:
    #                 k = k - n
    #             if k == i:
    #                 break
    #             arr[j] = arr[k]
    #             j = k
    #         arr[j] = temp
    #     print(arr)

    def reverseArray(self,arr, start, end):
        while (start < end):
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end = end - 1
        print(arr)



if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    array2 = [1, 2, 3, 4, 5, 6, 7]
    rotation = ArrayRotation()
    rotation.oneByOneRotation(array,2)
    d = 2
    n = len(array2)
    # rotation.jugglingRotation(array,3,2)
    rotation.reverseArray(array2, 0, d - 1)
    rotation.reverseArray(array2, d, n - 1)
    rotation.reverseArray(array2, 0, n - 1)

