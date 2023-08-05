# # # is and equal equal "==" are both comparision operator
# # # is is used to compare the exact location of the object in the memory
# # # == is used to compare the values of the 2 objects are same
# # a = [1,2,43]
# # b = [1,2,43]
# # # for this above list the is operator is false and == true 
# # print(a is b)
# # print(a == b)

# # for this both is and == are true as only one time 3 is stored into memory so is is true and == is 
# # true as both the values are the same
# a = 3
# b = 3
# print(a is b)
# print(a == b)

# # so as per tuple is immutable so only one memeory space is used so is is also true
# a = (1,2)
# b = (1,2)
# print(a is b)
# print(a == b)

a = None
b = None
print(a is b)
print(a is None)
print(a == b)

