def g(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>b and c>a):
        return c
    
a=int(input("enter a::"))
b=int(input("enter b::"))
c=int(input("enter c::"))

print(g(a,b,c))