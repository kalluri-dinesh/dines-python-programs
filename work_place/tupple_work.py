#Tuple: an ordered collection of heterogeneous elements encloses by using parentheses ()

#it is immutable

#we can access tuple elements by using indexing and slicing

# aa=(1,2,3,3,4,3)
# print(type(aa))
#
# print(dir(aa))  #'count', 'index'
#
# print(aa.count(3))
#
# print(aa.index(4))
#
# print(aa[4])

# c = -1
# for i in aa:
#     c=c+1
#     if i==3:
#         print(c,end=" ")


# students=[]
# def add_student(name):
#     students.append(name)
# def display_students():
#     for student in students:
#         print(student)
# add_student("dinesh")
# add_student("reddy dino")
# display_students()


class student:
    def __init__(self,name):
        self.name=name
    def display(self):

        print(f"student name:{self.name}")
student1=student("dinesh")
student2=student("reddy")
student1.display()
student2.display()


# try:
#     a=int(input("enter a number: "))
#     print("you entered:",a)
# except ValueError:
#     print("oops that was not a valid number.")



# try:
#     a=int(input("enter a number: "))
#     b=int(input("enter another number: "))
#     result=a//b
#     print("result:",result)
# except ValueError:
#     print("invalid input!please enter numbers only.")
# except ZeroDivisionError:
#     print("cannot divisible by zero")


# try:
#     a=int(input("enter a number: "))
#     print("you entered: ",a)
# except ValueError:
#     print("enter a valid number")
# else:
#     print("no errors occurred")
# finally:
#     print("this will print always")


import datetime
print(datetime.datetime.now())


# class student():
#     name="dinesh"
#     age=24
#     marks=9.5
# s1=student()     #s1 is an object
# print(s1.name)
# print(s1.age)
# print(s1.marks)

class python_class():
    a=5
    def output(self):
        print(self.a)
b=python_class()
c=python_class()
b.output()
c.output()
print(b.a)

#inheritance

#single inheritance

"""
class parent():
    def display(self):
        print("i am parent")
class child(parent):
    def displayc(self):
        print("i am child")
c=child()
c.displayc()
c.display()
"""

#multilevel inheritance

'''
class grandfather():
    def gf(self):
        print("i am grand father")
class father(grandfather):
    def fath(self):
        print("i am father")
class child(father):
    def disp(self):
        print("i am child")
b=child()
b.disp()
b.fath()
b.gf()
'''
#multiple inheritance

'''
class father():
    def displaya(self):
        print("i am father")
class mother():
    def displayb(self):
        print("i am mother")
class child(father,mother):
    def displayc(self):
        print("i am child")
a=child()
a.displayc()
a.displayb()
a.displaya()
'''
#hierarchiral inheritance
'''
class father():
    def display(self):
        print("i am father")
class child(father):
    def displaya(self):
        print("i am child")
class child1(father):
    def displayb(self):
        print("i am child 1")
class child2(father):
    def displayc(self):
        print("i am child 2")
a=child2()
b=child1()
c=child()
a.displayc()
a.display()
b.displayb()
b.display()
c.displaya()
c.display()
'''










