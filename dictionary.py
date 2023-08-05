# d = {
#     "chaitya" : "human being",
#     "spoon" : "object"
# }
# print(d["chaitya"])

# # it is used for mapping and dictionary is used in many ways

# j = {
#     175 : "chaitya",
#     176 : "dhyey",
#     178 : "parag",
#     174 : "dharmik"
# }
# print(j[175])

# # dictionary are ordered collection
# # dictionary are ordered

# print(j)
# print(j[175]) # this both are the same thing this will show error if the element does not exist
# print(j.get(174)) # this is also same but it will print none if the element is not present in

# # how to access all the keys

# print(j.keys()) # so in this the output will be dict_keys([175, 176, 178, 174])

# print(j.values())# this gives the vlaues dict_values(['chaitya', 'dhyey', 'parag', 'dharmik'])

# # this below one is mostly used with the f string
# for i in j.keys():
#     print(j[i])
# # this gives the output chaitya dhyey parag dharmik

# print(j.items()) # this gives the output 
# # dict_items([(175, 'chaitya'), (176, 'dhyey'), (178, 'parag'), (174, 'dharmik')])

# for i,j in j.items():
#     print(f"the vlaue corrosponding to the key {i} is {j}")
# # this also gives the same output as the above

# dictionary methord for update
k ={579:45,580:56,581:69,582:79}# this are the performences of the employes in percentages
p={222:67,586:99}
# k.update(p)
# print(k)

# k.clear() # used to clear the dictionary
# print(k)
# k.pop(579)
# print(k) # this means that the value 579 is pop from the dictionary

k.popitem() # this pops the last element from the dectionary
print(k)

# del k # error is been showm that the dictionary k is been deleted
# print(k) # NameError: name 'k' is not defined

e ={} # this gives the empty dictionary
print(type(e)) # the type of this is <class 'dict'>

