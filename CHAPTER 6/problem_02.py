marks1=int(input("enter marks 1"))
marks2=int(input("enter marks 2"))
marks3=int(input("enter marks 3"))

total_percentage=(100*(marks1+marks2+marks3))/300
print("u r marks is ",total_percentage)
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you r pass")
else:
    print("got failed")