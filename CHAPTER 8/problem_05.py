def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
a=int(input("enter a no.::"))
pattern(a)