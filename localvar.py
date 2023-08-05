x = 10 # global variable
print("global variable", x)
def my():
    global y # as global key word is used so the variable can now be used any where inside program
    global x
    x = 36
    y = 55 # local variable
    print("inside the function x", x)
    print("inside the function y", y)
my() # function call
# this local variable can only be used in the function or the body itself
print("outside the function y" , y) # so here error will be shown
print("outside the function x", x) # on the other hand global variable can be used any where inside the program