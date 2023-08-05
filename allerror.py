# # non compacticable data gives an error
# a= input("enter the value")
# print(f"multiplication table of {a} is")

# try:
#     for i in range(1,11):
#         print(f" {int(a)} X {i} = {int(a)*i}") # this is type casting 
# except Exception as e: # in this another way only write except:
#     print("invalid code so please ree do it")
#     print(e)
# # if in the input we give chaitya and it shows the error and program will not run any thing after 
# # for loop

# print("friend")
# print("the value might be fake")
# so this type of thing happen
# enter the valuechaiyta
# Traceback (most recent call last):
#   File "c:\chaitya3rd\class\new class\python\love babbar\pra.cpp\error.py", line 2, in <module>
#     a= int(input("enter the value"))
# ValueError: invalid literal for int() with base 10: 'chaiyta'

# so the try and except works as this
# enter the valuechaitya
# invalid literal for int() with base 10: 'chaitya' this is the exception e that is been printed
# and this are the 2 lines after the loop



# # another example
# try:
#     n = int(input("enter the vlaue"))
#     a =[6,3]
#     print(type(a)) # in this a is a list
#     print(a[n])
# except ValueError:
#     print("number entered is not an integer")
# except IndexError:
#     print("index error")

# in some of the cases where value in input is not present in a it gives 
# enter the vlaue7
# index error

################          finally                 #################
# try:
#     l = [1,5,6,8,9]
#     i =int(input("enter the value"))
#     print(l[i])
# except:
#     print("some error occured")

# # finally always gets executed either goes in except or try
# finally:
#     print("i am always executed")
#     # # this finally keyword is used more when the program has a function of error or so there it is 
#     # #a better use

# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")

# x = func1()
# print(x)

# # this above is the program for most use of finally

# ############ make custom errors and raise it ###############

# a= (input("enter the value"))
# # this is a custom error which is raised by raise
# if(a=="quit"):
#   pass
# elif(int(a)<5 or int(a)>9):
#   raise ValueError("value should be between 5 and 9")