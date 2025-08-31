p1="click this"
p2="buy now"
p3="free free"
p4="money here"

message=input("enter u r comment")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("is spam")
else:
    print("not a spam")