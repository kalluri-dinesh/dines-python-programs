import re

txt = "The rain in Spain_a"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "my name is dinesh"
x = re.search("vamsi", txt)
print(x)


a="i am from nellore"
b=re.findall("[a-n]",a)
print(b)


a1a="""dinesh reddy's phone number is 9100334187, call me any time if you want my pincode is 27 yep
CFO number (999)-333-7777"""

c=re.findall(r"\(\d{3}\)-\d{3}-\d{4}|\d{10}",a1a)
print(c)



def regular(a1):
        patterns = 'd'
        if re.search(patterns,  a1):
                return 'match found!'
        else:
                return 'Not matched!'

obj1=regular("my name is dinesh")
obj2=regular("Python Exercises.")
print(obj1)
print(obj2)



def expression(a):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns, a):
                return 'Found a match!'
        else:
                return('Not matched!')

print(expression("The quick brown fox jumps over the lazy dog."))
print(expression("Python_Exercises_1"))




name="my name is kalluru dinesh reddy"
a=re.search(r"\bk\w+",name)
print(a.string)

name="my name is kalluru dinesh reddy"
a=re.search(r"\bk\w+\s\w+\s\w+",name)
print("t",a.span())

name="my name is kalluru dinesh reddy"
a=re.search(r"\bd\w+",name)
print(a.group())

a="name dinesh redddy is my name"
b=re.search("am",a)
print(b)

details="my mail id is dineshreddy07777@gmail.com"
a=re.sub(r"\w*\W\w+","hello",details)
print(a)


a="""my name is ### dinesh reddy ( i am from 12 3 nellore @
my mail id is dineshredddy07777@gmail.com my mobile number is 9100334187.
"""
b=re.findall(r"\bd\w*\W\w*\.\w+",a)
c=re.findall(r"\bmy\w*[^\w]*",a)
print(b)
print(c)


name="my name is dinesh reddy kalluru"
a=re.search(r"\bn\w*",a)
print(a.group())

