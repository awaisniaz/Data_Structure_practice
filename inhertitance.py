class BaseClass:
    def sum(self,y):
        print("Hello bOY {}".format(y))


class SrecondBasedClass():
    def Sum2(self):
        print("Hello I am Second Function in my class")

class DriveClass(BaseClass,SrecondBasedClass):

    def system(self):
        print("I am Drived Class")
        print(DriveClass.mro())


if __name__ == '__main__':
    dc = DriveClass()
    dc.system()
    dc.sum("Awais NIAZ")
    dc.Sum2()

