class Father:
    def __init__(self):
        print("I am Fathe")
        super().__init__()


class Mother:
    def __init__(self):
        super().__init__()
        print("I am Mother")


class Son(Father,Mother):
    def __init__(self):
        print(Son.mro())
        super().__init__()
        print("I am Son")


if __name__ == '__main__':
    son = Son()