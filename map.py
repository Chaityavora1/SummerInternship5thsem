# # in this map filter and reduce are used and it is very important for the py
# ########## map ##########
# # def cal(x):
# #     return x*x*x
# # print(cal(2))
# l= [1,2,3,4,5,6]
# # newl = []
# # # in this we have appended the value from the l and cal it and from the function the returned ans is 
# # # stored in the newl
# # for i in l:
# #     newl.append(cal(i))
# # print(newl)

# # so in this the above from line 7 - 12 are the same code as 16-17 means 3 line efficient code using 
# # map it is very easy

# # map is always used as first (function and then , list of what from take the value)
# newl = list(map(lambda x: x*x*x,l))
# print(newl)

# ############  filter  ###############
# # in filter the only elements that are qualified form the list remains and other elements are 
# # filtered and this is how it works
# def filt(a):
#     return a>1

# newnewl = list(filter(filt,l))# so this filter help to filter the list the given way in the function
# # that we pass in the filter function
# print(newnewl)


########### use of reduce function
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum  
print(sum)