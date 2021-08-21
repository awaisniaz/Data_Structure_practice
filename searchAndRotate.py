def search(arr,n):
        for j in range(len(arr)):
            if(n == arr[j]):
                return j

if __name__ == '__main__':
    X = search([5, 6, 7, 8, 9, 10, 1, 2, 3],3)
    if X != None:
        print("Found at {}".format(X))