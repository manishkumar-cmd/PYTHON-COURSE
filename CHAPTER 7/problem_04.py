n=int(input("enter a no::"))
for i in range(2,n):
    if(n%i)==0:
        print("no is not prime")
else:
    print("no is prime")