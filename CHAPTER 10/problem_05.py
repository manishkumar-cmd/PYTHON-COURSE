from random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    
    def book(self,fro,to):
        print(f"Ticket fare in train no ::{self.trainNo} from {fro} to {to}")
    
    def getstatus(self):
        print(f"train no{self.trainNo} is running on time")
    
    def getFare(self,fro,to):
        print(f"Ticket fare in train no ::{self.trainNo} from {fro} to {to} is {randint(22,555)}")   
t=train(343)
t.book("jaipur","sikar")
t.getstatus() 
t.getFare("jaipur","rajasthan")        
        