#Data Hinding


class MyClass:
    __number = 0

    def add(self,increment):
        self.__number = self.__number + increment
        print(self.__number)



if __name__ == '__main__':
    myclass = MyClass()
    print(myclass._MyClass.__number)