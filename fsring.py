l = "hey my name is {} and i am from {}"
c = "india"
n = "chaitya"
print(l.format(n,c)) # this two values goes into the bracket

# k = "hey my name is {} and i am from {}"
# b = input("enter the name")
# v = input("enter the country")
# print(k.format(b,v)) # this is the same by user input

# fstring is the easy version of the same thing
print(f"hey my name is {n} and i am from {c} which is the best country")
# so this is the easiest methord to use in the python

# so this is also a best thing
p = 49.26589
y  = f"for the only value {p:.2f} dollers"
print(y)

print(type(f"{2*36}"))
print(f"{2*36}")

# if we want to show the string what is given as {name} insted of chaitya so do this
# retain the fstring with f string
print(f"my name is {{name}} and i am from {{country}}")

