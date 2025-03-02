# a=[1,3,2,6,4,8,2,1] #list
# b=(2,4,3,6,1)  #tuple
# c={"name":"krishna","place":"nellore"}
# s={3,2,5,4}
#
# #len ,Concatenation (+),Repetition(*) ,Membership (in, not in),Iteration(for or while)
# f=[2,4,3,5]  #list
# b_b=(7,8,4,3)  #tuple
# c_c ={"p_no":"9700962441"}
# print(len(s))
#
# print("Concatenation",c)
#
# # for i in a:
# #     print(i)print(i)
#
#
# a='dinesh'
# for i in a:
#     print(i)
#     if i=="s":
#         break
# else:
#     print("iterated over every thing")
#
# a="dinesh"
# for i in a:
#     if i=="s":
#         break
#     print(i)
# else:
#     print("iterated over every thing")
# a=[]
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         a.append(i)
# print(a)
# #
# #import random
#
# # import random
# # a=random.randint(1,10)
# # b=0
# # for i in range(1,10):
# #     print(i)
# # import random
# # a=random.randint(1,10)
# # b=0
# # while a!=b:
# #     c=int(input("enter a num:"))
# # print("well guessed!")
#
# # import random
# # a,b=random.randint(1,10),0
# # while a!=b:
# #     c=int(input("enter a number:"))
# # print("well done!")
#
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print("")
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print("")
#
#
# # a=input("enter a word:")
# # print(a[::-1])
#
#
#
# a=[]
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         a.append(i)
# print(a)
#
# # import random
# # a=random.randint(1,10)
# # b=0
# # while a!=b:
# #     c=int(input("enter a number"))
# # print("well guessed")
#
#
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print("")
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print("")
#
#
# a=input("enter a word:")
# print(a[::-1])
a=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        a.append(i)
print(a)



a=[i for i in range(1500,2701)if i%7==0 and i%5==0]
print(a)

# import random
# a=random.randint(1,10)
# b=0
# while a!=b:
#     b=int(input("enter a number between 1 and 9:"))
# print("well guessed:")



n=7
for i in range(1,n+1):
    for j in range(i):
        print("*",end="  ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end="  ")
    print()


# a=input("enter a word:")
# print(a[::-1])

a=(1,2,3,4,5,6,7,8,9)
e_n=[]
o_n=[]
e_c=0
o_c=0
for i in a:
    if i%2==0:
        e_n.append(i)
        e_c+=1
    else:
        o_n.append(i)
        o_c+=1
print(e_n)
print(o_n)
print(e_c)
print(o_c)



datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in datalist:
    print(i,type(i))




for i in range(6):
    if i==3 or i==6:
        continue
    print(i)

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)



a=3
b=4
a=[[i*j for j in range(b)]for i in range(a)]
print(a)


#
# a=int(input("enter no of rows:"))
# b=int(input("enter no of columns:"))
# a=[[i*j for i in range(b)]for j in range(a)]
# print(a)
#
#



a="DINESH reddy"
b=a.upper()
print(b)
print(a)
print(b)


a=[1,2,3]
print(sum(a))



def greet(name,nam):
    print("hello,",name)
    print("hi",nam)
greet("dinesh","vamsi")

a=lambda x:x*x
print(a(4))


add=lambda x,y:x+y
print(add(4,5))


bigger=lambda a,b:a if a>b else b
print(bigger(20,10))



a=lambda a:a*a
print(a(4))



add=lambda a,b:a+b
print(add(3,4))

bigger=lambda a,b:a if a>b else b
print(bigger(10,20))

is_even=lambda a:"even" if a%2==0 else "odd"
print(is_even(4))

# letter=lambda word:word[4]
# print(letter("dinesh"))



number=[1,2,3,4,5,6]
double=list(map(lambda a:a*2,number))
print(double)



numbers=(1,2,3,4,5,6,7,8)
even_numbers=list(filter(lambda a:a%2==0,numbers))
print(even_numbers)
#
#
#
# a=["kalluru","reddy","dinesh"]
# a.sort(key=lambda x:len(x))
# print(a)
#
# a=lambda b,c,d:b*c*d
# print(a(2,3,4))
#
# reverse=lambda a:a[::-1]
# print(reverse('dinesh'))
#
#
#
#
# a=["dinesh",1,1.20,"reddy","kalluru"]
# b=a[::-1]
# print(b)
#
# # for i in range(1,10):
# #     for j in range(i):
# #         print(i,end=" ")
# #     print("")
# for i in range(1,10):
#     for j in range(i):
#         print(i,end="   ")
#     print()
#
#
#
# for i in range(1,10):


a=10
b=20


def my_function():
    x=10
    print(x)
my_function()




y=20
def my_function():
    print(y)
my_function()
print(y)


def outer_function():
    z=10
    def inner_function():
        print(z)
    inner_function()
outer_function()



print(len("hello "))


a=5
def change_global():
    global a
    a=10
change_global()
print(a)














def f():
    a="dinesh"
    print(a)
f()
a="vinay"
print(a)

def inner_fun():
    a=10
    def outer_fun():
        print(a)
    outer_fun()

inner_fun()


a=[1,2,3,4,5]
square=list(map(lambda x:x**2,a))
print(square)




names=["dinesh","reddy","kalluru"]
upper_name=list(map(str.upper,names))
print(upper_name)


a=[1,2,3,4]
b=[5,6,7,8]
c=list(map(lambda x,y:x+y,a,b))
print(c)

a=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        a.append(i)
print(a)


# import random
# a=random.randint(1,10)
# b=0
# while a!=b:
#     b=int(input("enter a random number:"))
# print("well guessed!")



n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("")


# a=input("enter a word:")
# print(a[::-1])

a= (1, 2, 3, 4, 5, 6, 7, 8, 9)
eve_num=[]
odd_num=[]
eve_cou=0
odd_cou=0
for i in a:
    if i%2==0:
        eve_cou+=1
        eve_num.append(i)
    else:
        odd_num.append(i)
        odd_cou+= 1
print(eve_cou)
print(eve_num)
print(odd_cou)
print(odd_num)



a = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in a:
    print(i,type(i))


a=[1,2,3,4,5,"d","dinesh",2.50]
a.append("kalluru")
a.append("sai")
a.pop()
print(a)


#  0 1  2  3  4........positive indexing
a=[1 ,2 ,3 ,4 ,5]

#-5 -4 -3 -2 -1........negative indexing
print(a[1])
print(a[-2])


a=["a","b","c","d","e","f","g"]
# print(a[-6:-2:])
# print(a[0:6])
# a[3]="sai"
# print(a)
#
# a[4]="reddy"
# print(a)
# a.pop(4)
# print(a)
print(a[::-1])
a=[1, 2, 3]*4
print(a)

#
# for x in [1,2,3] : print (x,end = "    ")



a=[1,2,3,4,5,6,7]
print(dir(a))
# 'append', 'clear', 'copy', 'count',
# 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']



a=[1,2,3,4,5,6,7]
def even_number(i):
    return i%2==0
filtered_numbers=filter(even_number,a)
print(list(filtered_numbers))




words=["elephant","lion","dog","rat","cat","goat"]
filtered_words=filter(lambda word:len(word)<=3,words)
print(list(filtered_words))




def countdown(n):
    if n==0:
        print("done!")
        return
    print(n)
    countdown(n-1)
countdown(10)



print("hello world")


try:
    a=10/0
except ZeroDivisionError:
    print("cannot divide by zero")







width=5
height=10
area=width*height
print("area:",area)



a=[1,2,3,4,2,5,6,2,8,2]
print(dir(a))
#[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
a.append('dinesh')
print(a)

b=a.copy()
print(b)
b.clear()
print(b)
print(a.count(2))
a.extend("reddy")
print(a)
print(a.index(2))
a.insert(0,"sai")
print(a)
a.pop()
print(a)
a.remove("dinesh")
print(a)
a.reverse()
print(a)
b=[1,9,3,7,6,4,8,2]
b.sort()
print(b)
b.sort(reverse=True)
print(b)
a=1,2,3,4,"dinesh"
print(type(a))


a=(1,2,3,4,5,2,5)
print(type(a))
print(dir(a))
#'count', 'index'
print(a.count(4))
# print(a.index(7))


a="dinesh"
print(dir(a))
#, 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']








































