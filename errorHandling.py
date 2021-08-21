def errorHandling():
    a = [1,2,3]
    try:
       print("Second Element is  =  %d"%(a[1]))
       print("Third Element is  =  %d"%(a[3]))

    except:
        print("Hold tight something went wrong")


def fun(a):
    if a<4:
       b = a/(a-3)
    print("Value of b is {}".format(b))





if __name__ == '__main__':
    errorHandling()

    try:
        fun(10)
        fun(5)
        raise NameError('I am Getting Raised')
    except ZeroDivisionError:
        raise
        print("Zero Division Error Occured and Handler")
        raise
    except NameError:
        print("NameError Occured and Handler")
        raise
    except UnboundLocalError:
        print("UnboundLocalError")
        raise

# If exception is not raised by Try block than executed
    else:
        print("I am Calling now ,you have any problem now")

# Always Executed
    finally:
        print("I am Finally Block")
