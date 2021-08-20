x = ["Awais niaz","Rabia Khanam","Usman Niaz","Zain Ul Abideen","Tayyab Niaz","Qurat Ul Ain"]
for i,n in enumerate(x,start=400):
    print("{}  {}".format(i,n),end='\n')


y = [1,2,3,4,5]
a = [3,4,5,6,7]
b = [8,8,9,0,6]

for i in zip(y,a,b):
    print(i)