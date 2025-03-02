#1. Write a Python program to find those numbers which are divisible by 7 and  5,
# between 1500 and 2700 (both included).

a=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        a.append(i)
print(a)

#2. Write a Python program to guess a number between 1 and 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again
# until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random

target_num= random.randint(1, 10)
guess_num=0                              #------------->
while target_num != guess_num:   # 2 !=0
    guess_num=int(input("Enter No.")) #  5
print("Well Done")


#3. Write a Python program to construct the following pattern, using a nested for loop.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()                 #--------------------->need explanation
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#4. Write a Python program that accepts a word from the user and reverses it.

a=input("enter your word: ")
print(a[::-1])

#5. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

a=(1,2,3,4,5,6,7,8,9)

e_n=[i for i in a if i%2==0]
o_n=[i for i in a if i%2!=0]

print(e_n,o_n)

e_n=[]
e_c=0
o_n=[]
o_c=0
for i in a:
    if i%2==0:
        e_n.append(i)
        e_c+=1
    else:
        o_n.append(i)
        o_c+=1
print("even numbers are:")
print(e_n)
print("count of even numbers is:")
print(e_c)
print("odd numbers are:")
print(o_n)
print("count of odd numbers is:")
print(o_c)

#6. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

a=[1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in a:
    print(i,type(i))

#7. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

a=range(6)
for i in a:
    if i==3 or i==6:
        continue
    print(i)

#8. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

a=0
print(a)
b=1
print(b)
for i in range(1,9):  #-------------------->need explanation
    c=a+b
    print(a+b)
    a=b
    b=c

#9. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz"
# instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five,
# print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

#11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
#
# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
a=3
b=4
a=[[i*j for i in range(b)]for j in range(a)]#--------------->need explanation

                # [[(0,1,2)*(0,1,2,3)]]
                # [[0,0,0,0],[0,1,2,3],[0,2,4,6]]
print(a)

#11. Write a  Python program that accepts a sequence of lines (blank line to terminate)
# as input and prints the lines as output (all characters in lower case).
while True:
    a = input('Enter text: ')
    if len(a) == 0:
        print('You entered nothing')#---------->explanation
        break
    else:
        print(a.lower(), end = '\n')


































