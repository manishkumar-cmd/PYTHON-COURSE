class jee:
    name="manish"
    language="py"
    salary=2000000
    
    def __init__(self):
        # self.name=name
        print(" ia ma creating obj")
    def getInfo(self):
        print(f"the lang is {self.language}.the salary is {self.salary}")
    
manish=jee()
# print(jee.name,jee.language,jee.salary)
manish.getInfo()
# manish.greet()

manish=jee()
manish.name="manish"
print(manish.name,manish.salary)