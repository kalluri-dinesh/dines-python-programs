#23 table

#23*1=23
#23*2=46
#

# a=int(input("enter your table:"))  #23
# b=int(input("enter your range:"))  #10
# for i in range(b,0,-1):
#     print(a,'*',i,'=',a*i)


a=[1,2,3,5,6,7,3,4,9]
#op=[2,1,5,3,7,6,4,3,9]
#[3,2,1,7,6,5,9,4,3]
#import pdb;pdb.set_trace()
for i in range(0,len(a)-1,2):
    a[i],a[i+1] =a[i+1],a[i]

print(a)

for i in range(0,len(a),3):
    a[i],a[i+1],a[i+2]=a[i+2],a[i+1],a[i]
print(a)
