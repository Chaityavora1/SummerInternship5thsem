# f = open('myfile.txt' , 'r') # so it opens the file myfile.txt and other r is the mode in which it 
# # opens the file which is read
# # so there are 3 modes      1 read       2 write      3 append
# # it is readable as we have oppened it into the read mode and if we convert the above r into w
# # then it will give error to the text as above is write mode and how to read in write mode
# text = f.read() # it will print the textual content of the file
# print(text)
# f.close()



#######################    writing to a file           #############################
# f = open('myfile.txt','w')
# f.write('chaitya')
# f.close()
# with open('myfile.txt' , 'a') as f: # with the use of this we donot need to use the f.close 
# # command and this is append function that appendas the write thing after the text is over
#     f.write("hey i am inside the file")
# f = open('my.txt','w')
# f.write('56,89,54,')
# f.write('98,7,8,')
# f.write('99,95,94')
# f.close()
try:
    i = 0
    f = open('myfile.txt', 'r')
    while True:
        i=i+1
        line = f.readline()
        # print(line)
        if not line:
            # print(line, type(line))
            break
        m1 = line.split(",")[0]
        m2 = line.split(",")[1]
        m3 = line.split(",")[2]
        print(f"marks of student {i}in math are {m1}")
        print(f"marks of student {i} in science are {m2}")
        print(f"marks of student {i} in gk are {m3}")
    f.close()
except FileNotFoundError:
    print("The file 'my.txt' does not exist.")
