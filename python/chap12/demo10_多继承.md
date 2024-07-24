```py
class FatherA:
    def __init__(self,name):
        self.name=name
    def showA(self):
        print("父类A中的方法")

class FatherB:
    def __init__(self,age):
        self.age=age
    def showB(self):
        print("父类B中的方法")

class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
        FatherA.__init__(self,name) #给name赋值
        FatherB.__init__(self,age) #给age赋值
        self.gender=gender


if __name__ == '__main__':
    son=Son("陈梅梅",20,"女")
    son.showA()
    son.showB()
```
