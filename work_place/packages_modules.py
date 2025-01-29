# a=10
# print(a)
# a=12
# print(a)

#
# NAme='sai'
# print(NAme)
#
# age=20
# print(age)
#
#
# _gender='male'
# print(_gender)
#
# x,y=1,2
# print(x)
# print(x,y)

# x,y,z=1,2,3
# print(x,y,z)
#
# x,y,z=1,2,4
# print(x,y,z)
#
# a,b,c=0
# print(x,y,z)

# a='dinesh'
# print(type(a))
#
# b=20
# print(type(b))
#
# c=2.0


# 1=3
# print(a1)

#memory management

# a=10
# b=a
# a=20

#dynamic allocation
#garbage collection
#reference  counting
# a=10
# b=a
# c=b
# d=b
#
# a=10




# a=10
# b=5
# c=a>=b
# print(c)

#A,B,C,L,A,I,M


# a=10
# if not a<20:
#     print('false')
# else:
#     print('true')


# a=10
# a//=4
# print(a)



# a=[1,2,3]
# b=a
# c=b
# print(a is c)
# print(a is b )
#
# a="dinesh"
# b="dinesh"
# c="reddy"
# print(a is not b)
# print(a is not c)
# x="sai"
# y="sai"
# z="reddy"
# print(x is not y)
# print(x is not z)




# a=10
# print(id(a))
#
# b=5
# print(id(b))
#
# a=10
# print(id(a))
#
# a=10
# a=15
# b=16
# print(a)
#
# a='dinesh'
# print(id(a))
# b='dinesh'
# print(id(b))
# a='reddy'
# print(id(a))
# c="reddy"
# print(id(c))
#
#
#
# print(dir(a))
#
# print(type("reddy"))

a=[]
for i in range(5):
    print(i)
    a.append(i**2)
print(a)


a=[i**2 for i in range(10)]
print(a)

a=[]
for i in range(10):
    if i%2==0:
        a.append(i)
print(a)

a=[i for i in range(10) if i%2==0 if type(i)==str]
print(a)

a={1,2,3,4,2,5,6}
print(type(a))
b={i*2 for i in a }
print(b)


import collections
from collections import Counter
a=Counter('rrdggfhfjghjgddtjghjjhkh')
print(dir(a))
# print(a.most_common())

a={'name':'dinesh','age':24,'gender':'male'}
print(dir(a))
#'clear', 'copy', 'elements', 'fromkeys', 'get', 'items', 'keys', 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'total', 'update', 'values'
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


a=range(10)
print(a)
print(list(a))

# a="dinesh reddy"
# b=iter(a)
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
#
# a="kalluru"
# b=iter(a)
# print(b.__next__())
# print(b.__next__())
# print(list(b))

# a=[1,2,3,4,5,6,7,8]
# b=iter(a)
# print(b.__next__())
# print(list(b))


def my_gene():
    yield "kalluru"
    yield "dinesh"
    yield "reddy"
a=my_gene()
print(a.__next__())
print(a.__next__())
print(a.__next__())


a=("dinesh")
b=a.ljust(20,'*')
print(b)


a={1,2,3,'dinesh'}
print(type(a))





























