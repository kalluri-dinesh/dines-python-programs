# String: Strings are sequences of characters.
# 2. Python strings are "immutable" which means they cannot be changed after they are created.
# 3. To create a string, put the sequence of characters inside either single quotes, double
# quotes, or triple quotes and then assign it to a variable.
# access characters from String, use indexing or slicing
from pandas.core.dtypes.cast import maybe_downcast_numeric

aa="KRISHNA reddy"
# print(type(aa))
# print(dir(aa))


#'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

cc=aa.capitalize()   #Converts the first character of a string into Upper case
print(cc)            #Krishna reddy from nellore
dd =aa.casefold()    #Returns casefolded string. Converts Uppercase to lowercase.
print(dd)            #krishna reddy from nellore
ff=aa.center(17)     #Returns a new copy of the string after centering it in a field of length width
print(ff)
a=1
while a<=10:
    print(a)
    a+=1

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('Inside else block of while loop.')

count = 0
while count <= 5:
    print(count)
    count += 1
    if count==4:
        break
else:
    print('Inside else block of while loop.')



while True:
    a=input("type 'exit'to stop:")
    if a=="exit":
        break




a=(1,2,3,4,5,6,7,8,9)
even_number=[]
odd_number=[]
even_count=0
odd_count=0
for i in a:
    if i%2==0:
        even_count+=1
        even_number.append(i)
    else:
        odd_count+=1
        odd_number.append(i)
print("even numbers are")
print(even_number)
print("odd numbers are")
print(odd_number)
print(even_count)
print(odd_count)

a= [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in a:
    print(i,type(i))
















