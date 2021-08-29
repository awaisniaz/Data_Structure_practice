from collections import defaultdict

Dict = {1:'GEEKS',2:'For',3:'GEEKS'}
def defaultValue():
    return 'Not Found Please Insert First'
defult = defaultdict(defaultValue,Dict)
print(defult[4])

# Chain Map

# python chain map contain multiple dictionaries at one Place

from  collections import ChainMap

d1 = {'a':10,'b':"45"}
d2 = {'a':10,'b':"45"}
d3 = {'a':10,'b':"45"}

c = ChainMap(d1,d2,d3)

print(c.keys())
print(c.values())
print(c.maps)


from collections import namedtuple
student = namedtuple('Student',['Name','Age','DOB'])
S = student('Awais Niaz',23,'1995/11/11')
print(S.Name)


# Deque in Python

# Double Ended Queue

from collections import deque

data = deque(['Name','Age','DOB'])
data.append(['Awais Niaz',32,'1195/32/22'])
data.appendleft(['Usman Niaz',21,'1995/21/21'])
print(data.index('Name'))