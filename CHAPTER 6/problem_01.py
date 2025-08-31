a1=int(input("enter no 1"))
a2=int(input("enter no 2"))
a3=int(input("enter no 3"))
a4=int(input("enter no 4"))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is larger",a1)
    
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is larger",a2)
    
elif(a3>a2 and a3>a1 and a3>a4):
    print("a3 is larger",a3)
    
# elif(a4>a2 and a4>a3 and a4>a1):
    
else:
    print("a4 is larger",a4)
    
    