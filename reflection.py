x = 6
def testFunction():
    print("Test 1")


y = testFunction

if(callable(y)):
    print("Y is Callable")
else:
    print("Y is not Callable")


if(callable(x)):
    print("X is callable")
else:
    print("X is Not Callable")


print(dir(y))
