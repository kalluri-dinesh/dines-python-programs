#STRING

# a="python"
# print(a[1])
#
# print(a[0::2])
# b="dinesh"
# print(b)
# del (b)
# print(b)


a="sai"
print(dir(a)) #'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
# 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# a="dinesh"
# b=a.capitalize()
# print(a)
# print(b)
#
#
# a="DIneSH reddy"
# b=a.casefold()
# print(a)
# print(b)


#
# a="reddy"
# b=a.center(10,'+')
# print(b)
#
# a="dinesh"
# print(a.rjust(10,"@"))
# print(a.ljust(20,"*"))
a="dinesh reddy"
print(a.startswith("r"))

# a="di\tn\te\tsh"
# print(a.expandtabs(7))

a="my name is dinesheeee"
print(a.count("name"))



a="reddyd"
print(a.rfind("m"))

b="dinesh reddy kalluru"
print(b.index("r"))

a="dinesh reddy kalluru"
print(b.rindex("r"))

c="formts {} version  of the {} "
print(c.format("specified","string"))

a="kalluru dinesh reddy"
print(a.split("d",2))
b="kalluru dinesh reddy"
print(a.rsplit("d",2))


a="   dinesh   "
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())

import collections
print(dir(collections))
from collections import Counter
a=['apple','banana','apple','mango','banana','apple']
b=Counter(a)
print(b)

#




from collections import namedtuple



a=namedtuple('a',["name","age","city"])
b=a(name="dinesh",age="24",city="nellore")
print(b.name)
print(b.city)
print(b.age)

from collections import ChainMap

a={"a":1,"b":2}
b={"b":3,"c":4}
c=ChainMap(a,b)
print(c['a'])
print(c["b"])
print(c["c"])



# class SimpleNumbers:
#     def __int__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num >5:
#             raise StopIteration
#         value=self.num
#         self.num+=1
#         return value
# a=SimpleNumbers()
# for num in a:
#     print(num)


class Dinesh:
    def __init__(self,start,end):
        self.a=start
        self.end=end
    def __iter__(self):
        return self


 #'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
# 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# a="kalluru dinesh reddy"
# print(a.split("d",2))
# b="kalluru dinesh reddy"
# print(a.rsplit("d",2))
#
#
# a="   dinesh   "
# b=a.rstrip()
# print(b)
#
#
# a={}
# a["name"]="dinesh"
# a["place"]="nellore"
# print(a)
#
#
a={"name":"dinesh","age":24,"place":"nellore"}
# print(a["place"])
# print(a["age"])
# print(dir(a))
# # 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# b=a.copy()
# print("b",b)
# print("a",a)
# b.clear()
# print(b)
# a.update({"language":"python"})
# print(a)
# c=a.values()
# print(c)
# d=a.keys()
# print(d)
# e=a.items()
# print(e)
a.pop("age")
print(a)
a.popitem()
print(a)
f=a.get("place")
print(f)


g=a.setdefault("name","place")
print(g)

a={"name":"dinesh","age":24}
b=a.fromkeys("kvr")
print(a.update(b))
a['name']="kvr"
print(a)

import logging
print(dir(logging))


a={'name':'dinesh','age':24,'gender':'male'}
b=a.fromkeys('kdr',1)
print(a)
print(a.update(b))
print(a)

print(dir(a))
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

b={'name':'sai','age':23}
print(b)
b.clear()
print(b)
a={1,2,3,4,5,6,7,8,9,9,9,9,9}
print(type(a))
print(a)
a={'d','i','n','e','s','h'}
print(a)

b=set("dinesh")
print(type(b))

c={}
print(type(c))


a={1,2,'dinesh'}
b=a.add(6)
print(a)
c=a.add(7)
print(a)
d=a.update([3,4,5,'dino'],(1,3,4,'m'),{'money','python',1,2})
print(a)

b=a.remove(2)
print(a)
print(dir(a))

#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection','intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
# 'union', 'update']

a={'dinesh','reddy','kalluru'}
b=a.add(1)
print(a)
a={1,2,3,4}
b={1,2,5,6}
c=b.difference(a)
print(c)
a={1,2,3,4,5,6}
b={1,2,3,7,8,9}
print(a)
print(b)
# print(a.difference(b))
c=b.difference_update(a)
print(a)

print(b)
a={1,2,3,4,5,9,10,11}
b={1,2,3,4,5,6,7}
c=a.symmetric_difference_update(b)
print(a)

print(6+4/2-(1*2))







