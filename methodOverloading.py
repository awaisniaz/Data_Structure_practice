# Method Overloading

class MyClass:
    def sum(self,*args):
        sum = 0
        for i in args:
            sum = sum + i
        return sum
    
    
if __name__ == '__main__':
    myClass = MyClass()
    print( myClass.sum(19,15))