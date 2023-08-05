def isgreater(a,b):
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")

d= 9
v= 15
isgreater(d,v)
# in this *num reacts as a tuple 
def avg(*num):
    sum = 0
    print(type(num))
    for i in num:
        sum = sum + i
    print("average of the tuple is" , sum / len(num))

avg(6,5,7,9)
# if there we take is as **num then it takes as a dictionary and take the output of string as form of 
# dictionary

# in function we mostly use return insted of print
a = 5


def value(a):
    print(type(a))
    for i in range (0,a):
        return i    
m = value(5)
print(m)
