#List: an ordered collection of heterogeneous elements encloses by using square broses

#it is mutable  [C U R D]

#we can access list elements by using indexing and slicing

aa=[1,3,4,5,9,8,7,5,2.3,'kvr']
print(aa[-7:-1:2])
#print(type(aa))   #<class 'list'>
#print(dir(aa))  # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
                # 'remove', 'reverse', 'sort']
aa.append("dinesh")  #it can add  value at last position of list
print(aa)
print(aa.count(5))  #it can count the element in list

bb= aa.copy()   #it can copy and create new variable
print("bb",bb)
bb.clear()   #it can cler the all values in side list
print(bb)
aa.extend("vamsi")  #it can split the string into elements and adding into existing list
print(aa)
print(aa.index('kvr')) #it can print the  1st index of value
aa.remove("kvr") #it can remove the value from list
print(aa)
aa.insert(9,"krishna reddy") #it can insert the value in particular index
print(aa)
aa.pop()  # it can delete last element in list
print(aa)
aa.pop(9)  # it can delete element at 9 index position
print(aa)
aa.remove(2.3)
print(aa)

cc=[2,5,1,4,8,5,67,45]
cc.sort() #it can print the values in ascending order(only applicable for integers
print(cc)
cc.sort(reverse=True)#used to print the values in descending order
print(cc)

print(aa.reverse())# it can reverse the entire list
print(aa)

a=['ba','cc','a','r','g','y']
a.sort()
print(a)
