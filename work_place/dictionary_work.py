# aa={'name':"dinesh","age":24,"place":"nellore","mob.no":9100334187}
# print(type(aa))
# print(dir(aa))
# #'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# print(aa)
# b=aa.copy()
# print(b)
# b.clear()
# print(b)
# print(aa.get("place"))
# print(aa.items())
# print(aa.keys())
# aa.pop('mob.no')
# print(aa)
# aa.popitem()
# print(aa)
# cc="dinesh"
a={'name':'dinesh','age':20,'gender':'male','plac':'nellore'}
print(a)
print(type(a))
print(dir(a))
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
b=a.copy()
print(b)
b.clear()
print(b)
print(a.get('gender'))
print(a.items())
print(a.keys())
a.pop('plac')
print(a)
a.popitem()
print(a)
print(a.values())
#  a.update(.fromkeys('reddy',20)
a.update(b.fromkeys('dino',20))
print(a)
print(a.setdefault('name'))


