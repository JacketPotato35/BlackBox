class Question():
    def __init__(self):
        self.a=0
        self.question=[("#use modulus to find the remainder when a=7 and is divided by 3","a=7"),("%","=","4"),("1") ]
    def insert_self_code(self,string):
        for i in self.question[0]:
            string+=i
            return string
ques=Question()
a="hello"
a=ques.insert_self_code(a)
print(a)