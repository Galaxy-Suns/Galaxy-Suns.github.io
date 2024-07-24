```py


print(dir(object))

class Person: #默认继承object,所以object可以省略不写
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"大家好我叫{self.name},我今年{self.age}")

    def __str__(self):
        return '这是一个人类,具有name,age两个实例属性'
if __name__ == '__main__':

    per=Person("陈梅梅",20)
    print(dir(per))

    print("---------------------------")
    print(per) #当直接输出对象名时，默认直接调用__str__()方法
    print(per.__str__())

    print("---------------------------")
    # Person类的方法，调用__dir__()方法
    #以下两句代码功能相同，都是查看对象具有的属性和方法
    print(per.__dir__())
    print(dir(per))

```
