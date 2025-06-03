from functools import reduce
a=[1,2,3,4]
pro = reduce(lambda x,y:x*y,a)
print(pro)