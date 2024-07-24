```py


s='hello,hello'
print(s.index('lo')) #3
print(s.find('lo')) #3
print(s.rindex('lo')) #9
print(s.rfind('lo')) #9



#print(s.index('k')) #ValueError: substring not found
print(s.find('k')) #-1 find,rfind不会抛异常，找不到时输出-1
#print(s.rindex('k')) #ValueError: substring not found
print(s.rfind('k'))

```
