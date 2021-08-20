class MyClass:
    number = 0
    name = "Awais Niaz"


def main():
    me = MyClass()
    me.name = "Usman Niaz"

    print("{}  {} ".format(me.name,me.number))


if __name__ == '__main__':
    main()