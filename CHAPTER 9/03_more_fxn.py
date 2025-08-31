# f=open("file.txt")
# lines=f.readlines()
# print(lines,type(lines))
# f.close()

f=open("file.txt")
# line1=f.readlines()
# print(line1,type(line1))
# line2=f.readlines()
# print(line2,type(line2))
# line3=f.readlines()
# print(line3,type(line3))
# line4=f.readlines()
# print(line4,type(line4))
# f.close()


line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()