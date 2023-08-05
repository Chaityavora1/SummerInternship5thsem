# marks = [1,2,3,4,5,6,7,8,9,10]
# print(marks[-5])
# print(marks[len(marks)-5])
# print(marks[10-5])
# print(marks[5])
# so  this is the list and this is how we use it
# print(marks[:]) 
# this two are the same as the output are the same
# print(marks)  
# this is also the same

# lst = [i for i in range (4)]
# print(lst)
# o = [i*i for i in range(9)]
# print(o)
# p = [i*i for i in range(10) if(i%2 == 0)]
# print(p)

u = [11,2,3,6,48,96,55]
print(u)
u.append(7) # so in this append add the value at the last which we append 
# print(u)
# u.sort()
# print(u)
u.sort(reverse=True) # this will sort in desending order and always use the T insted of t
print(u)
u.reverse() 
print(u)# this reverse the list

print(u.index(6)) # is 2 same value in the list then it will give the index of 1st occuring value
print(u.count(2)) # counts how many times the value occurs in the list
m = u.copy()
print(m) # so this copies the list in some new list

u.insert(1,899) # in this we have inserted 899 at the 1st index
print(u)
u.sort()
print(u)
t = [11,26,8859,5623]
# t.extend(u) in this extend methord we added the u elements after the t elements 
# [11, 26, 8859, 5623, 2, 3, 6, 7, 11, 48, 55, 96, 899]
print(t)
# or other methord to concatinate is
k = t+ u
print(k) # so this is another methord to merge 2 list
n = [22,6,9,456]
# this is the methord to add the values of the 2 list
result = [x+y for x,y in zip(n,t)]
print(result)

