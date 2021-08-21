import userDefinedException
class MainMenu:
    try:
        raise(userDefinedException(3*2))
    except userDefinedException as ude:
        print("A new Exception occured {}".format(ude.value))