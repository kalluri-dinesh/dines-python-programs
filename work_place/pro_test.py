def A(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner

def B(a, b):
    return a/b

obj=A(B)
print(obj(1,2))

##################################################################################

def A(fun):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return fun(a, b)
    return inner

@A
def B(a, b):
    return a/b

B(1,2)





a=["1","2","3","4"]
b="abc"
print(b.join(a))


a="dinesh"
print(dir(a))


def my_decorator(wrapper):
    def dinesh(a,b):
        print("my name is ",a)
        a=wrapper()
        print('my name is ',b)
        return a
    return dinesh

@ my_decorator
def decorator():
    return "hello"
#print(decorator())

obj=decorator("dinesh","vamsi")
print(obj)
# obj=my_decorator(decorator)
# obj(1,2)

def dinesh(fun):
    def reddy(a,b):
        a=fun()
        return a.upper()
    return reddy


@dinesh
def dinesh_reddy():
    return "kalluru dinesh reddy"
# print(dinesh_reddy())
obj=dinesh_reddy("reddy","dinesh")
print(obj)





class UpperCase:
    def __init__(self,func):
        self.a=func
    def __call__(self, *args, **kwargs):
        b=self.a(*args,**kwargs)
        return b.upper()

@UpperCase
def greet():
    return "hello, world"
print(greet())



def dinesh_reddy(fun):
    def wrapper():
        print("my name is dinesh reddy...")

        print("my name is vamsi...")
        return fun()
    return wrapper()
# @dinesh_reddy
def greet():
    return "hello..."
obj=dinesh_reddy(greet)
print(obj)












































