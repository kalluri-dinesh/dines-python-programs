a="yellow-red-orange-green-black-purple-gold"
def words():
    b=a.split("-")
    b.sort(reverse=True)
    print('-'.join(b))
words()

def squares():
    a=[i**2 for i in range(1,31)]
    print(a)
squares()

def square(a):
    b=[]
    for i in a:
        b.append(i**2)
    print(b)
square(range(1,31))



