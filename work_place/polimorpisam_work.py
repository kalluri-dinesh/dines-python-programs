class A:
    def product(self,a,b):
        print(a*b)
    def product(self,a,b,c):
        print(a*b*c)

obj=A()
obj.product(1,2,3)


# class UserDetails:
#     def __init__(self,name,date_of_birth,ph_num):
#         self.name=name
#         self.date_of_birth =date_of_birth
#         self.ph_num=ph_num
#     def MyDetails(self):
#         return {"name":self.name,"dob":self.date_of_birth,"pn":self.ph_num}
#
# class BankDetails(UserDetails):
#     def GetBankDet(self,user_det):
#         #print("user det",user_det['name'])
#         #this data you are getting from bank table
#         #selct * form SBIBANK_table where name=user_det['name'] and dataofbirth=user_det['dob']
#         # aa=SBIBANK_det.objects.filter(name=user_det['name'],dataofbirth=user_det['dob'])
#         ban_det_obj={"a/c":12345677,"ifsc":"SBIN2244","epin":"2312"}
#         if ban_det_obj:
#             return {"valid_user":True,"ac_bal":100,'bank':'unio'}
#         else:
#             return {"valid_user": False, "ac_bal": None,"bank":None}
#
# class BankTran(BankDetails):
#     def bank_t(self,data):
#         print(data)
#         if data['valid_user'] ==True:
#             try:
#                 bank = data['bank']
#                 a = data['ac_bal']
#                 if a and bank == 'sbi':
#                     print('withdraw your money')
#                 if a < 50 and bank !='sbi':
#                     raise ValueError("insufficient balance")
#                 else:
#                     print("this ATM not support for withdrew")
#             except ValueError as a:
#                 print(a)
#             else:
#                 print("'loading...")
#             finally:
#                 print("your transaction has been completed please collect your card")
#
#         else:
#             print("invalid user")
#
#
#
# obj=BankTran("dinesh","10-2-1998","9700962441")
#
# obj_new=obj.GetBankDet(obj.MyDetails)
#
# obj.bank_t(obj_new)
#
# # class UserDetails:
# #     def __init__(self,name,date_of_birth,ph_num):
# #         self.name=name
# #         self.date_of_birth =date_of_birth
# #         self.ph_num=ph_num
# #     def MyDetails(self):
# #         return {"name":self.name,"dob":self.date_of_birth,"pn":self.ph_num}
#
#
# class UserDetails:
#     def __init__(self,name,date_of_birth,ph_num):
#         self.name=name
#         self.date_of_birth =date_of_birth
#         self.ph_num=ph_num
#     def MyDetails(self):
#         return {"name":self.name,"dob":self.date_of_birth,"pn":self.ph_num}
#
# class BankDetails(UserDetails):
#     def GetBankDet(self,user_det):
#         #print("user det",user_det['name'])
#         #this data you are getting from bank table
#         #selct * form SBIBANK_table where name=user_det['name'] and dataofbirth=user_det['dob']
#         # aa=SBIBANK_det.objects.filter(name=user_det['name'],dataofbirth=user_det['dob'])
#         ban_det_obj={"a/c":12345677,"ifsc":"SBIN2244","epin":"2312"}
#         if ban_det_obj:
#             return {"valid_user":True,"ac_bal":100,'bank':'unio'}
#         else:
#             return {"valid_user": False, "ac_bal": None,"bank":None}
#
# class BankTran(BankDetails):
#     def bank_t(self,data):
#         print(data)
#         if data['valid_user'] ==True:
#             try:
#                 bank = data['bank']
#                 a = data['ac_bal']
#                 if a and bank == 'sbi':
#                     print('withdraw your money')
#                 if a < 50 and bank !='sbi':
#                     raise ValueError("insufficient balance")
#                 else:
#                     print("this ATM not support for withdrew")
#             except ValueError as a:
#                 print(a)
#             else:
#                 print("'loading...")
#             finally:
#                 print("your transaction has been completed please collect your card")
#
#         else:
#             print("invalid user")
#
#
#
# obj=BankTran("dinesh","10-2-1998","9700962441")
#
# obj_new=obj.GetBankDet(obj.MyDetails)
#
# obj.bank_t(obj_new)


class UserDetails:
    def __int__(self,name,date_of_birth,ph_no):
        self.name=name
        self.dob=date_of_birth
        self.phno=ph_no
    def MyDetails(self):
        return {"name":self.name,"dob":self.dob,"ph_no":self.phno}
class  BankDetails(UserDetails):
    def GetBankDetails(self,user_det):
        bank_obj={"a/c":123456789,"ifsc":"CNRB00057","epin":1234}
        if bank_obj:
            return{"valid_user":True,"acc_bal":100,"bank":"canara"}
        else:
            return{"valid_user":False,"acc_bal":None,"bank":None}
class BankTransaction(BankDetails):
    def bank_tran(self,data):
        print(data)
        if data["valid_user"]==True:
            try:
                bank=data["bank"]
                bal=data["acc_bal"]
                if bal and bank=="canara":
                    print("withdraw your money")
                if bal<50 and bank!="canara":
                    print("insufficient funds")
                else:
                    print("this atm is not supported")
            except ValueError as a:
                print(a)
            else:
                print("loading....")
            finally:
                print("your transaction has been completed please collect your card")
        else:
            print("invalid user")
# obj=BankTransaction("dinesh")
# new_obj=obj.GetBankDetails(obj.MyDetails)
# obj.bank_tran(new_obj)


















































