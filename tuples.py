# so this the way to use the tuples
# p = (1,5,6,9,10)
# print(type(p) , p)
# but only one value then?
# j = (1)
# print(type(j) , j)
# it will change to <class 'int'>
# but if we do
# l = (1,)
# print(type(l) , l)
# this will give us <class 'tuple'> (1,)
# in list we can change the value but in tuple it is not possible
# if 5 in p:
#     print("yes the value is present in p tuple")

# in tuples also we can use the [:] way and also the negativ indexing

#       tuples methords that we can use

# c = ("india" , "africa" , "spain" , "germany" , "egypt" , "ukrane")
# temp = list(c)  #this is the way to typecast the tuple to the list by another variable
# temp.append("russia")   # in this it add the element at the last of the list
# print(temp)
# temp.pop() # in this it pops the last element of the list
# print(temp)
# print(type(temp))
# temp[2] = "netherland"
# print(temp)
# c= tuple(temp)
# print(type(c))
# print(type(temp))
# print(c)

# c1 = ("india" , "africa" , "spain" , "germany" , "egypt" , "ukrane")
# c2 = ( "pok" , "usa" , "uk" , "la" , "turky")
# c3 = c1 + c2
# print(c3) # this concatinate the two tuples with each other into a 3rd variable

v = (5,5,6,9,5,5,62,45,2,2,5)
print(v.count(5)) # return the number of count the value is present\

print(v.index(5,3,9)) # this means that from 3rd index to 9th index where the value 5 is present
# so the solution for this is 4
# also we can find the length 
############ so the main thing is that we have to convert tuple to list and then change the ###########
############            changes and then again change it to tuples                          ###########
