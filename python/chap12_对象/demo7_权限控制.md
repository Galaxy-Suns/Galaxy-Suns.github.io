```py
class Student:
    # 首尾双下划线，表示特殊方法，一般系统定义
    def __init__(self,name,age,gender):
        self._name=name #以单下划线开头，表示受保护的成员，只能类本身，或子类访问
        self.__age=age #以双下划线开头，表示私有的，只能类本身访问
        self.gender=gender #普通的实例属性，在类的外部和类的内部以及子类都可以访问

    def _fun1(self): #以单下划线开头，表示是受保护的方法
        print("子类和本身可以访问")

    def __fun2(self): #以双下划线开头，表示私有的
        print("只有定义的类可以访问")

    #这是一个普通的方法，谁都可以访问，在类的外部使用对象名打点访问
    #在类的内部使用 self 打点访问
    def show(self):
        self._fun1() #类本身去访问受保护方法
        self.__fun2() #类本身访问私有方法
        print(self._name) #类本身访问受保护的实例属性
        print(self.__age) #类本身访问私有的实例属性

if __name__ == '__main__':
    #创建一个Student类对象
    stu=Student("陈梅梅",20,'女')
    #访问受保护的实例属性
    print(stu._name)

    #访问私有的实例属性
    #print(stu.__age) 程序报错，超过类的定义范围

    #访问受保护的实例方法
    stu._fun1()

    #访问私有的实例方法
    #stu.__fun2()

    #可以使用以下的形式访问类对象的私有成员
    print(stu._Student__age)
    stu._Student__fun2() #不建议```
