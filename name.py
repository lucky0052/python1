import random
class name:
    guess = random.randrange(1,10)
    def __init__(self,name):
        self.name = name

    @property
    def id(self):
        return self.ids

    @id.setter
    def id(self,ids):
        self.ids = ids
        return self.ids


    def display(self):
        return f'{self.name}{name.guess}{self.id}'

stu1 = name('Lucky')
stu1.id = "53"
print(stu1.display())


