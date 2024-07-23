```py
class A:
    pass
class B:
    pass
class C(B,A):
    def __init__(self,name,age):
        self.name=name
        self.age=age

if __name__ == '__main__':
    a=A()
    b=B()
    c=C("陈梅梅",20)
    print(a.__dict__) #对象的属性字典
    print(c.__dict__)
    print(a.__class__) #对象所属的类
    print(b.__class__)
    print(c.__class__)
    print(A.__bases__) #类的父类，结果是一个元组
    print(C.__bases__)
    print(A.__base__) #类的父类，如果继承多个父类，结果为第一个父类
    print(C.__base__)
    print(A.__mro__) #[<class '__main__.A'>, <class 'object'>] A类继承了object类
    print(C.__mro__) #[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>] C类继承了A类和B类，A,B又继承了object
    #用于获取类的子类
    print(A.__subclasses__()) #A的子类C
    print(C.__subclasses__()) #C没有子类，空列表```
