import time 
# t = time.strftime('%H:%M:%S')
# print(t)
# h = int(time.strftime('%H'))
# print(h)
h = int(input("enter the value of time"))
if(h > 0 and h< 12):
    print("good morning")
elif(h>=12 and h<17):
    print("good afternoon")
elif(h>=17 and h<20):
    print("good evening")
else:
    print("good night")
# m = int(time.strftime('%M'))
# print(m)
# s = int(time.strftime('%S'))
# print(s)