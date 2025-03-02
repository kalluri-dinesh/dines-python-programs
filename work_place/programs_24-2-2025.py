#1
a=[1,2,3,4,5,6,7,8,9]
even=[i for i in a if i%2==0]
print(even)

a=[1,2,3,4,5,6,7,8,9]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)
#2
pairs=[(i,j) for i in range(3) for j in range(3)]
print(pairs)

a=range(3)
b=range(3)
c=[]
for i in a:
    for j in b:
        c.append([i,j])
print(c)
#3
matrix=[[1,2,3],[4,5,6],[7,8,9]]
a=[j for i in matrix for j in i]
print(a)

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)
#4
a=[1,2,3,-4,5,-6,-7,8]
b=[i if i>=0 else 0 for i in a]
print(b)


a=[1,2,3,-4,5,-6,-7,8]
b=[]
for i in a:
    if i>=0:
        b.append(i)
    else:
        if i<0:
            b.append(0)
print(b)
#5
keys=['name','age','city']
values=['dinesh',24,'nellore']
pairs={i:j for i,j in zip(keys,values)}
print(pairs)

keys=['name','age','city']
values=['dinesh',24,'nellore']
a=dict(zip(keys,values))
print(a)

d={}
for i in range(0,len(keys)):
    d[keys[i]]=values[i]
print(d,"d----->")

#6
square=[i**2 for i in range(5)]
print(square)

a=range(5)
b=[]
for i in a:
    b.append(i**2)
print(b)
#7
a=['kalluru','dinesh','vamsi','reddy']
b=[i.upper() for i in a]
print(b)

a=['kalluru','dinesh','vamsi','reddy']
b=[]
for i in a:
    c=i.upper()
    b.append(c)
print(b)
#8
a="hello dinesh"
b=[i for i in a if i in "aeiou"]
print(b)

a="hello dinesh"
b=[]
for i in a:
    if i in "aeiou":
        b.append(i)
print(b)
#9
a=['dinesh','vamsi','redddy']
b=[i[::-1] for i in a]
print(b)

a=['dinesh','vamsi','redddy']
b=[]
for i in a:
    b.append(i[::-1])
print(b)
#10
a=[i for i in range(1,51) if i%3==0 and i%5==0]
print(a)

a=range(1,51)
b=[]
for i in a:
    if i%3==0 and i%5==0:
        b.append(i)
print(b)
#11
a=[1,2,3,4,5]
b=[1,6,5,8,9]
c=[i for i in a if i in b]
print(c)

a=[1,2,3,4,5]
b=[1,6,5,8,9]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)


























