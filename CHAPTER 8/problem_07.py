# def rem(l,word):
def r(l,word):
    n=[]
    
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["manish","herry","rohan","an"]
print(r(l,"an"))