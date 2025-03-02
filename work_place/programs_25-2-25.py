
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
a={'name':'dinesh','age':24,'gender':'male'}
print(a)
b=a.copy()
print(b)
b.clear()
print(b)
c=a.values()
print(c)
d=a.popitem()
print(a)
e=a.pop('age')
print(a)
f=a.keys()
print(f)
g=a.items()
print(g)
h=a.get('name')
print(h)
a={'name':'dinesh','age':24,'gender':'male'}
b=a.setdefault('place','nellore')
print(a)
c=a.fromkeys('abc',123)
print(a.update(c))
print(a)

a={i:i**2 for i in range(1,6)}
print(a)

a={}
for i in range(1,6):
    a[i]=i**2
print(a)

a={i:i**3 for i in range(1,11) if i%2==0}
print(a)

a={}
for i in range(1,11):
    if i%2==0:
        a[i]=i**3
print(a)

a="dinesh reddy"
b={i:a.count(i) for i in a}
print(b)

a="dinesh reddy"
b={}
for i in a:
    b[i]=a.count(i)
print(b)



keys=['name','age','gender']
values=['dinesh',24,'male']  #--------------->
pairs={i for i in zip(keys,values)}
print(pairs)

keys=['name','age','gender']
values=['dinesh',24,'male']
pairs=dict(zip(keys,values))
print(pairs)

a={'telugu':45,'hindi':80,'english':72,'maths':47,'science':52}
b={i:j for i,j in a.items() if j>50}
print(a.items())
print(b)

a={'telugu':45,'hindi':80,'english':72,'maths':47,'science':52}
b={}
for i,j in a.items():
    if j>50:
        b[i]=j
print(b)

a={'name':'dinesh','age':24,'gender':'male'}
b={j:i for i,j in a.items()}
print(b)

a={'name':'dinesh','age':24,'gender':'male'}
b={}
for i,j in a.items():
    b[j]=i
print(b)

a=['dinesh','reddy','kalluru']
b={i:len(a) for i in a}
print(b)

a=['dinesh','reddy','kalluru']
b={}
for i in a:
    b[i]=len(a)
print(b)

a={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}
b={i:j for i,j in a.items() if j%2==0 }
print(b)

a={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}
b={}
for i,j in a.items():
    if j%2==0:
        b[i]=j
print(b)


a={chr(i):i for i in range(27,68)}
print(a)

a=range(27,68)
b={}
for i in a:
    b[chr(i)]=i
print(b)

a="hello dinesh hello everyone"
c=a.split() #['hellow','dinesh','hellow']
print(' '.join(c))
b={i:a.count(i) for i in a.split()} # ['hellow','dinesh','hellow']
print(b)

a="hello dinesh hello everyone"
b={}
for i in a.split():
    b[i]=a.count(i)
print(b)

students={'dinesh':50,'vamsi':70,'sai':35,'nc':54,'teja':22}
passed_students={i:j for i,j in students.items() if j>=50}
print(passed_students)

students={'dinesh':50,'vamsi':70,'sai':35,'nc':54,'teja':22}
a={}
for i,j in students.items():
    if j>=50:
        a[i]=j
print(a)

import math
a={i:math.sqrt(i)for i in range(1,5)}
print(a)

from math import sqrt
a={i:sqrt(i)for i in range(1,5)}
print(a)

a=1,2,3,4,5
b={}
for i in a:
    b[i]=sqrt(i)
print(b)



















