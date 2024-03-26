'''
class computer:
    def __init__(self):
        self.__price=2000
        self._p=25
        self.a=10
        print("__init__ is ",self.__price,self.a)

    def sell(self):        
        print("sell is",self.__price,self._p,self.a)

class laptop(computer):
    def lap(self):
        self._p=200
        self.a=15
        print("laptop is",self._p,self.a)

l=laptop()
l.sell()
l.lap()
l.sell()


from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def func1(self):
        print("This is abstract method func1")

    @abstractmethod
    def func2(self):
        print("This is abstract method func2")

class anotherClass(Abstract):
    def func1(self):
        super().func1()
        print("This is first derived method")
        
    def func2(self):
        print("this is second derived method")
        super().func2()

ob=anotherClass()
ob.func1()



#create a abstract class 'Bank' by using methods bank_info(),offers() and interest
#Interest() must be abstract method
#create two child class 'SBI' and 'PNB'
# with 'SBI' class print 'this is sbi bank'
# with 'PNB' class print 'this is pnb bank'


from abc import ABC, abstractmethod

class Bank(ABC):
    
    @abstractmethod
    def interest(self,i):
        pass

    def bank_info(self,bankname):
        self.bankname=bankname
        print ("Bank Name is ",self.bankname)

    def offers(self):
        print("this is offers info")

class banktype(Bank):

    def interest(self,i):
        self.i=i
        print("This is interest method",self.i)        

sbi=banktype()
sbi.bank_info('SBI')
sbi.interest(10)
sbi.offers()
        
pnb=banktype()
pnb.bank_info('PNB')
pnb.interest(11.5)
pnb.offers()

-create a class employee and add some attributes like name,
age, salary.
-now add two methods show_age() to print the age
and show_name() to print the name
-create one child class of employee and print the salary
using the method show_salary()
salary variable must be protected.

'''

class Employee:

    
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self._salary=salary

    def show_name(self):
        print("Name of the employee",self.name)

    def show_age(self):
        print("Age of the employee",self.age)

class showdetails(Employee):

    def show_salary(self):
        print("Salary of the employee",self._salary)
    
    

ob=showdetails("Satya",45,10000)
ob.show_name()
ob.show_age()
ob.show_salary()



    

    

        

    

    

        






