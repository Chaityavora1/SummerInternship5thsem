# class Employee:
#     def __init__ (self,n,id):
#         self.n = n
#         self.id = id

#     def show(self):
#         print(f"the name of the employee is {self.n} and id {self.id}")

# class programmer(Employee): # this the way inheritance is done
#     def showl(self):
#         print("the default laungage is python")

# c = Employee("chaitya vora" , 52)
# c.show()
# # c.showl() #this gives the error as emplyee has not inherited the programmer but this below will not
# # not give error as programmer has inherited the employee
# c2 = programmer("anil" , 598)
# c2.showl()
# c2.show()

###########################             access modifiers                                  ########################### 
# types of access modifiers
# public
# private
# protected

# this by default is public 
# class E:
#     def __init__(self):
#         self.n = "chaitya"

# a = E()
# print(a.n)

# # in python there is nothing as private,public,protected
# #so here __(2times underscore is used to make it private)
# class E:
#     def __init__(self):
#         self.__n = "chaitya"

# a = E()
# # print(a.__n)# to access this private this will give an error 
# # so methord to do it is 
# print(a._E__n) # so to access private do it this way obj._class name __ n

# # to see the methords that are avalable for the object can be access by this 
# print(a.__dir__())
# # ['_E__n', '__module__', '__init__', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__',
# #  '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__',
# #  '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

# Name mangling:-(it is same that i used before)
# Name mangling in Python is a mechanism that modifies the names of class members to avoid name
#  clashes between different classes. It is primarily
#  used to provide a form of name privacy or to enforce encapsulation within a class.

 
# # protected
# class S:
#     def __init__(self):
#         self._n = "h" # if the value is already given so do not write it in the bracket
#         # else write if you have to take input at the time of object construction
    
#     def _f(self):      # this is a protected methord
#         return "chaityahvora"
    
# class Su(S): # inheritance class
#     pass

# obj1 = S()
# obj2 = Su()

# # calling by the object of the S class
# print(obj1._n)
# print(obj1._f())
# # calling by the object of the Su class
# print(obj2._n)
# print(obj2._f())

############      Static methord   ###############
# class M:
#     def __init__(self,num):
#         self.num = num
#     def sum(self,n):
#         self.num = self.num +n
    
#     @staticmethod # with the help of this @staticmethod we do not need to 
#     # use the self and without it also the program works
#     def add(a , b):
#         return a+ b
    
# a = M(5)
# print(a.num)
# a.sum(6)
# print(a.num)

################   instance and class variable################   
# type 1 in here all the  variable used are the instance variable and that 
# can be changed.
# class
# class E:
#     def __init__(self ,n):
#         self.n = n
#     def show(self):
#         print(f"the name of the employee is {self.n}")
    
# emp1 = E("chaitya")
# emp1.n = "nimit"# this is another way by which i can change the variable
# # value
# emp1.show()

# type 2
class E:
    comp = "br" # so here the comp is the class variable and it is by default given 
    # into the class.
    no = 0
    def __init__(self ,n):
        self.n = n
        E.no += 1
    def show(self):
        print(f"the name of the employee is {self.n} and the company in which i work is {self.comp} has a staff of {self.no}")
    
emp1 = E("chaitya")
emp1.comp = "apple india"
E.show(emp1)
# so for this as we changed the comp it is apple india but for the below we have not 
# changed it do it will take the by default class variable which is br
emp2 = E("n")
emp2.show()
print(E.comp)
# so first the instance variable are checked if present then show it first 
# if not present then find the class variable

# this is same as local and global variable it will first give chance to local 
# and then to the global

