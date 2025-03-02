# class Parent:
#     my_name="krishna"
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def PFun(self,name):
#         print("i am "+name +"father of below child like "+self.a)
#     def MyDetails(self):
#         print("krishna ")
#
#
# class Child(Parent):
#     def CFun(self,name):
#         print("my name is " + name +" i am child of above parent")
#
#
# class SubChild(Child):
#     def SCFun(self):
#         print("i am "+ self.a +" i am sub child")
#
# # obj=Child('vamsi','reddy')
# # print(dir(obj))
# #
# #
# # obj.PFun("Ratna reddy")
# # obj.CFun("dinesh")
#
# obj=SubChild("vamsi","krishna")
#
# obj.PFun("ratna reddy")

class UserDetails:
    def __init__(self,name,date_of_birth,ph_num):
        self.name=name
        self.date_of_birth =date_of_birth
        self.ph_num=ph_num
    def MyDetails(self):
        return {"name":self.name,"dob":self.date_of_birth,"pn":self.ph_num}

class BankDetails(UserDetails):
    def GetBankDet(self,user_det):
        #print("user det",user_det['name'])
        #this data you are getting from bank table
        #selct * form SBIBANK_table where name=user_det['name'] and dataofbirth=user_det['dob']
        # aa=SBIBANK_det.objects.filter(name=user_det['name'],dataofbirth=user_det['dob'])
        ban_det_obj={"a/c":12345677,"ifsc":"SBIN2244","epin":"2312"}
        if ban_det_obj:
            return {"valid_user":True,"ac_bal":100,'bank':'unio'}
        else:
            return {"valid_user": False, "ac_bal": None,"bank":None}

class BankTran(BankDetails):
    def bank_t(self,data):
        print(data)
        if data['valid_user'] ==True:
            try:
                bank = data['bank']
                a = data['ac_bal']
                if a and bank == 'sbi':
                    print('withdraw your money')
                if a < 50 and bank !='sbi':
                    raise ValueError("insufficient balance")
                else:
                    print("this ATM not support for withdrew")
            except ValueError as a:
                print(a)
            else:
                print("'loading...")
            finally:
                print("your transaction has been completed please collect your card")

        else:
            print("invalid user")



obj=BankTran("dinesh","10-2-1998","9700962441")

obj_new=obj.GetBankDet(obj.MyDetails)

obj.bank_t(obj_new)





class Dinesh:
    def Get_my_details(self):
        name ="dinesh"
        dob ="18-10-1999"
        ph=989898989
        edu="BTech"
        saly=2000
        return ({"name":name,"dob":dob,"ph_no":ph,"education":edu,"salary":saly})

class RatnaReddy:
    def Get_Father_Details(self):
        name = "ratna reddy"
        dob = "18-10-1999"
        ph = 989898989
        edu = "BTech"
        saly = 2000
        return ({"name": name, "dob": dob, "ph_no": ph, "education": edu, "salary": saly})



class Vamsi:
    def Get_brother_details(self):
        name = "vamsi"
        dob = "18-10-1999"
        ph = 989898989
        edu = "BTech"
        saly = 2000
        return ({"name": name, "dob": dob, "ph_no": ph, "education": edu, "salary": saly})



class MyFamilyDetails(Dinesh,Vamsi,RatnaReddy):
    pass

obj=MyFamilyDetails()

print(obj.Get_Father_Details())
print(obj.Get_brother_details())
print(obj.Get_my_details())


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
print(add(5,3))
print(subtract(5,3))



a=set()
for i in range(5):
    a.add(i*2)
print(a)



