# this code is for doc-string and pep 8

# python doc string are the string literals that apperar right after the defination of the function 
# ,methord,class ,of modules

def square(n):
    '''take in a number n,return the square of n'''
    # this above line is a doc string which tells us about our function
    print(n**2) # this (**) meand the square

square(5)
print(square.__doc__) # this line prints me the doc string and so it is similar to the comments 
# in the function 
# to use doc string in function above the body i have to insert this line 
# diffrence (by changing the comments the program does not change but by changing the docstring 
# program changes)

def k(m):
    print(m)
    '''ahdfihuiwg'''
print(k.__doc__) 

k(6)
# so in this above function the doc string is not present ans the 1st line should of the doc string 
# which is not the case in this so the output is None

############              pep 8             ###############
# pep 8 provides the guid line and best practice for the python code

#  import this
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

