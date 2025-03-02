class Myclass:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30


class MyChild(Myclass):
    def get_data(self):
        return self._b

obj=MyChild()
print("aaa",obj.get_data())
print(obj.a)
print(obj._b)
print(obj._Myclass__c)