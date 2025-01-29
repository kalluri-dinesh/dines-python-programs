#Tuple: an ordered collection of heterogeneous elements encloses by using parentheses ()

#it is immutable

#we can access tuple elements by using indexing and slicing

aa=(1,2,3,3,4,3)
print(type(aa))

print(dir(aa))  #'count', 'index'

print(aa.count(3))

print(aa.index(4))

print(aa[4])

# c = -1
# for i in aa:
#     c=c+1
#     if i==3:
#         print(c,end=" ")