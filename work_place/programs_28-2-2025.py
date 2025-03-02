def biggest(b,c,*a):
    return max(a)
print(biggest(5,3,9,3,4))

def add(*a):
    return sum(a)
print(add(8,2,3,0,7))

def multiply(*a):
    total=1
    for i in a:
        total*=i
    return total
print(multiply(8,2,3,-1,7))

def reverse(a):
    a=a[::-1]
    return a
print(reverse("1234abcd"))

# num=int(input("enter a number"))
# def abc():
#     if num in range(1,50):
#         print("entered num is in the given range")
#     else:
#         print("entered num is not in the range")
# abc()



a=range(1,11)
def bcd(i):
    if i in a:
        return "entered number is in the given range"
    else:
        return "out of range"
print(bcd(10))


def letters_count(a):
    upper_count=0
    lower_count=0
    special_char=0
    for i in a:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
        else:
            special_char+=1
    print("upper case:",upper_count)
    print("lower case:",lower_count)
    print("special case:",special_char)
letters_count("dinesh,REDDY#@$:;")

def unique_elements(*a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b
print(unique_elements(1,2,3,3,3,4,5))

def prime_number():
    a= int(input('Please Enter the value: '))
    if a==2 or a==3 or a==5 or a==7:
        return "Prime_Number."
    elif a%2==0 or a%3==0 or a%5==0 or a%7==0 :  #-------->need explanation
        return "Not_Prime_Number."
    else:
        return "Prime_Number."
print(prime_number())

def even_num(a):
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)
    return b
print(even_num([1,2,3,4,5,6,7,8,9]))

def perfectNumber(n):
    k=[i for i in range(1,n) if n%i==0]
    if sum(k)==n:
        return (n,' is perfect number')
    else:                                   #------------>need explanation
        return (n,' is not perfect number')
print(perfectNumber(72))


def palindrome(a):
    if a==a[::-1]:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
palindrome("madam")


def pangram(a):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    if a in alphabet:
        print("this is a pangram")   #-------------------------
    else:
        print("this is not a pangram")
pangram("the quick brown fox jumps over the lazy dog")






















a_l=[1,22,43,'abc','gd',54,67,82,97,76,876,345,234,373456734657,374373,7467347456,354327324,9394839891324,43654234]
b=0
for i in a_l:
    if type(i) !=str:
        if i >b:
            b=i
print(b)

c=sorted([i for i in a_l if type(i) !=str])[-1]
print(c)

c=[1,2,3,4,5,'jkj',6,7,8,9,2,32,323,23,23,23,23,23,23,23232]
a=0
for i in c:
    if type(i) ==str:
        c.remove(i)
print(sum(c))

c=sum([i for i in c if type(i) !=str])
print(c)









