'''定义 python 中的 类'''

class Student:  # Student为类的名称（类名）由一个或多个单词组成,每个单词的首字母大写其余小写
    pass

# python中一切皆对象，Student是对象吗？内存有开空间吗？
print(id(Student)) # 6616848
print(type(Student)) # <class 'type'>
print(Student) # <class '__main__.Student'>