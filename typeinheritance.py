# ##################### single inheritance ######################
# class A:
#     def __init__(self, name, s):
#         self.name = name
#         self.s = s
    
#     def ms(self):
#         print(f"Sound is made by {self.name} animal")

# class D(A):
#     def __init__(self, name, b):
#         A.__init__(self, name, s="Dog")
#         self.b = b

#     def ms(self):
#         print("Bark!")

# d = D("dog", "pitbull")
# d.ms()

# a = A("ice wolf", "wolf")
# a.ms()

# class C(A):
#     def __init__(self, name, b):
#         A.__init__(self,name,s= "cat")
#         self.b = b
#     def ms(self):
#         print("meow meow")

# c = C("cat" , "lazy fast")
# c.ms()

# ##################### multiple inheritance ######################
# class E:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"the name is {self.name}")
# class D:
#     def __init__(self,d):
#         self.d =d 
    
#     def show(self):
#         print(f"the dance doing is {self.d}")

# class DE(D,E):
# # this methord will print the function or the class that comes first
# # in this example (E,D) the solution is the name is shivgami devi
# # this all depends on this (E,D) if (D,E) then the output will be 
# # the dance doing is bharat natiyam
#     def __init__(self,d, name):
#         self.d =d 
#         self.name = name


# o = DE("bharat natiyam" , "shivgami devi")
# print(o.name)
# print(o.d)
# o.show()
# print(DE.mro()) # output is [<class '__main__.DE'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]


# ##################### Multilevel inheritance ######################
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# # o = Dog("tommy", "Black")
# # o.show_details()
# # print(GoldenRetriever.mro())

# p = GoldenRetriever("tomboy" , "blue")
# p.show_details()

# ##################### Hybride inheritance ######################
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass
# this is a hybride inheritance