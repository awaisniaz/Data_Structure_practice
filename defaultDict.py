from collections import defaultdict

Dict = {1:'GEEKS',2:'For',3:'GEEKS'}
def defaultValue():
    return 'Not Found Please Insert First'
defult = defaultdict(defaultValue,Dict)
print(defult[4])