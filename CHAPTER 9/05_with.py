# f=open("file.txt")
# print(f.read())
# f.close()

#this same can be writen with sttemnt


with open("file.txt") as f:
    print(f.read())