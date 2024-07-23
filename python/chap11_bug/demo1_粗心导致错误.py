'''粗心导致错误'''

age=input('请输入你的年龄')
print(type(age))
if int(age)>=18: # if age>=18:
    print('成年人...')

i=0
while i<10:
    print(i) # print（i）
    i+=1