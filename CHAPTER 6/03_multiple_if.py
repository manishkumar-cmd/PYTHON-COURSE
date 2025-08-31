a=int(input("enter your age"))


#start if 1
if(a%2==0):
    print("a is even")
#end if 1
#start if 2
if(a>=18):
    print("u can get access")
elif(a<0):
    print("write valid age plz")
elif(a==0):
    print("its zero bro")
else:
    print("you are a kid")
#end if 2    
print("end of program")