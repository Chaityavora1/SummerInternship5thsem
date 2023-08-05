
# # class Car:
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model

# #     def start_engine(self):
# #         print(f"The {self.brand} {self.model}'s engine is starting.")

# # # Creating objects (instances) of the Car class
# # car1 = Car("Toyota", "Camry")
# # car2 = Car("Honda", "Civic")

# # # Accessing object attributes
# # print(car1.brand)  # Output: Toyota
# # print(car2.model)  # Output: Civic

# # # Calling object methods
# # car1.start_engine()  # Output: The Toyota Camry's engine is starting.
# # car2.start_engine()  # Output: The Honda Civic's engine is starting.
# class Person:
#     name = "chaitya"
#     occupation = "developer"
#     net = 10

#     def info(self): # in here self is used for the object that has been called eg- there is only a
# # BUT IF there is also a b then self deffers from the call from a,b,c,d........
#         print(f"{self.name} is a {self.occupation}") # in this self is also similar to this 
# # keyword in java
# a = Person()
# # a.name = "subh"
# # a.occupation = "accountant"
# print(a.name, a.occupation)
# a.info()


# ######################## constructor in oop very important  #########################
# class Person:
#     def __init__(self,n,o): # this is a constructor and it is used by the keyword __init__
# # it always return none
# # default constructor is used when only self is used
# # this above constructor is parameterised constructor
#         print("hey i am a person")
#         self.name = n
#         self.occ = o
#     def info(self): # in here self is used for the object that has been called eg- there is only a
# # BUT IF there is also a b then self deffers from the call from a,b,c,d........
#         print(f"{self.name} is a {self.occ}")
# a = Person("chaitya" , 1000)
# b = Person("chuni" , 1025)
# a.info()
# b.info()  
# a.name = "subh"
# a.occupation = "accountant"
# print(a.name, a.occupation)
# a.name = "diviya"
# a.occuptaion = "hr"
# a.info()

# this is define of instance (in the above case a and b are the instances of objects)
# In object-oriented programming (OOP), an instance refers to a specific occurrence or individual 
# object that is created based on a class. It represents a unique
# realization of the class's blueprint, with its own set of attribute values and state.


# ##### decorators : it is a function which takes another function,updatas it and then return it #####
# In Python, a decorator is a special kind of function that can modify
#  or enhance the behavior of another function without changing its source code.
#  It allows you to wrap additional functionality around a function, such 
#  as logging, timing, or input validation, without modifying the original function directly.
# def g(f):
#     def mf():
#         print("good morning")
#         f()
#         print("thanks for visiting")
#     return mf

# @g # this is the first(1) methord for decorator
# def he():
#     print("hello")

# def a():
#     print(a+b)

# he()
# # g(he)()# this is another methord(2) for decorator

# def time_decorator(func):
#     def wrapper():
#         import datetime
#         print(f"Current time: {datetime.datetime.now()}")
#         func()
#         print(f"Current time: {datetime.datetime.now()}")
#     return wrapper
# @time_decorator
# def greet():
#     print("Hello, world!")
# greet()

#### this is another program for the use of decoding

# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func._name_} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func._name_} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b


############          getter and setter      #############
# getter and setter are also a very good option for encapsulation
# Certainly! In Python, getters and setters are methods or functions used to 
# access and modify the values
# of an object's attributes. They provide a way to control
# how the attributes are accessed and updated, allowing for better encapsulation and data integrity.


class My:
    def __init__(self,v):
        self._v = v

    def show(self):
        print(f"value is {self._v}")
    
    @property # by using this @property we have created a getter function that can return the value
# from a function
# in this the @property is used if we want to return the value with complex calculation 
# such as here we have 10* self._v if we dont use the @property (getter) every time a new
# value will be printed in print(obj.t_v)
    def t_v(self):
        return 10* self._v
    
    # @t_v.setter
    # def t_v(self,new_v):
    #     self._v = new_v/10


obj = My(10)
# obj.t_v = 67
print(obj.t_v)
obj.show()
# in this getter and setter both the function name are the same.
# and by which we can set a value.

# define of template
# A template, in the context of OOP, provides a set of rules, attributes,
# and behaviors that objects created from it will possess.
# It outlines the common characteristics and functionalities that the
# objects will have, but it doesn't represent a specific instance or individual object itself.


