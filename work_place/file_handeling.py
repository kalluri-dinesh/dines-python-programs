# 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush',
# 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline',
# 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write',
# 'write_through', 'writelines'
# aa=open('my_file_new.txt')
# n=int(input("enter line number:"))
# for i in range(n):
#     print(aa.readline(),end='')

# a=open("dinesh_file.txt","r")
# print(dir(a))
# 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty',
# 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines',
# 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
# print(a.read())
# print(a.readlines())
# print(a.readable())
# print(a.readline(),end="")
# print(a.readline())
# print(a.readline())
# a.close()
# print(a.readline())
# a=open("dinesh_file.txt","r")
# # print(dir(a))
# # print(a.fileno())
# # print(a.isatty())
# # print(a.read())
# # print(a.readable())
# print(a.readline())
# print(a.readline())
# print(a.readline())
# a=open("dinesh_file.txt","r")
# print(a.read())
# a=open("dinesh_file.txt","r")
# b=int(input("enter no of lines:"))
# c=0
# while c!=b:
# line=a.readline()
# print(line,end="")
# c+=1


# a="dinesh_file.txt"
# b=int(input("enter no of lines to read:"))
# c=open(a,"r")
# d=c.readlines()
# for i in d[:b]:
#     print(i,end="")
#
# c.close()

#
#
# a="dinesh_file.txt"
# b=int(input("enter number of lines to read:"))
# c=open(a,"r")
# for i in range(b):
#     d=c.readline()
#     if not d:
#         break
#     print(d,end="")
# c.close()

# aa=open("dinesh_file.txt","r")
# print(aa.readline())
# print(aa.readline())
# print(aa.readline())
# print(aa.readline())


# a="dinesh_file.txt"
# b=input("enter text to append:")
# c=open(a,"a")
# c.write(b+"\n")
# print(c)
# c.close()
# c=open(a,"r")
# d=c.read()
# c.close()
# print("\nUpdated file content:")
# print(d)
a=0
while a<5:

    print(a)
    a += 1

for i in range(10):
    if i==7:
        break
    print(i)



for i in range(10):
    if i==6:
        continue
    print(i)



































