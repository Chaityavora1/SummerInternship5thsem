# this is a normal function
# def d(x):
#     return x*2

# print(d(5))

# lambda function it is mostly used when we pass a function as an argument
d = lambda x: x*2
c = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3 # it will make it into double
print(d(5))
print(c(5))
print(avg(5,9,11))

# lambda best use
def f(fx,value):
    return 6+fx(value)
print(f(c,2)) # so in here in a function a function is passed and the value is returned
# it is a important function
s = lambda x: x*x
def h(n,val):
    return n(val)
print(h(s,4))