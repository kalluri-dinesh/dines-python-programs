def Default_args(a=1,b=2,c=3):
    d=a+b+c
    print(d)
Default_args(5,5)


def positional_args(b,a):
    c=a+b
    print(c)
positional_args(1,2)

def variable_no_of_args(*args):
    print(args)
variable_no_of_args(1,2,3,4.5,6,8,'kvr',89)


def keyword_args(**kwargs):
    print(kwargs)
keyword_args(name='krishna',place='nellore',ph=9700962441)


def all_args_in_one_fun(a=5,b=2,*args,**kwargs):
    global c
    global d
    c='nnnnnn'
    d='ssss'

    print(a)
    print(b)
    print(args)
    print(kwargs)
all_args_in_one_fun(1,2,3,4,5,6.4,'kvr','reddy',name='krishna',place='nellore',ph=9700962441)
c='dddd'
print(c)
print(d)
xx = (lambda a = 'hello', b = ' Welcome to': a + b + c)

aa=xx('hee','krishnareddy')
print(aa)
#
#
#
#


def dinesh_args(a=1,b=2,c=3):
    d=a+b+c
    print(d)
    dinesh_args(5,10)
#
#
#
#Default Arguments:-
def default_arguments(a=1,b=2,c=3):
    d=a+b+c
    print(d)
default_arguments(3,4)
#
#
#
#Positional Arguments:-
def positional_arguments(a,b,c):
    d=a+b+c
    print(d)
positional_arguments('dinesh',' ','reddy')
#
#
#
#Variable number of arguments(*args)
def variable_no_of_args(a,b,*args):
    print(a,b,args)
variable_no_of_args(1,2,3,5,'kdr',2.50,213)
#
#
#
#Keyord Arguments(**kwargs)
def keyword_arguments(a=4,b=6,**kwargs):
    print(a,b,kwargs)
keyword_arguments(1,name='dinesh',age='24',ph_no=9100334187,)
#
#
#
# a=lambda x,y,z:x+y+z
# a(1,2,3)
# a=(lambda a='hello',b=' welcome to',c='python':a+b+c)
#
# print(a('krishna'))
#
# a('hello','dinesh','reddy')
#
#
#
# a=10
# b=20
# c="krishna"
#
#
# def add_two_elements():
#     global a
#     a=12
#     b=13
#     c="reddy"
#     print("local",a+b)   #25
#
# add_two_elements()
#
# print("global",a+b)
#
#
# a=10
# b=20
# c=40
#
#
#
#
# a=lambda x,y,z:x+y+z
# b('dinesh','reddy','kalluru')
# print(a('dino'))
# a('hello','dinesh','reddy')
# print(a)
#
# a=110
# b=20
# c='dinesh'
#
# def addition():
#     a=10
#     b=30
#     global c
#     c='reddy'
#     print('local',a+c)
a=lambda x,y,z:x+y+z
a(1,2,3)
a=(lambda a='hello ',b='welcomes ',c='dinesh':a+b+c)
print(a('python '))




