```py


# ---------------trying-----------------
# 时间2021/8/20 15:11
'''多分支结构，多选一执行
从键盘录入一个整数成绩
90-100 A
80-90 B
70-80 C
60-70 D
60以下 E
'''
grade=int(input('请输入成绩'))
if 90<=grade<=100:
    print('查询结果为   A')
elif 80<=grade<90:
    print('查询结果为   B')
elif 70<=grade<80:
    print('查询结果为   C')
elif 60<=grade<70:
    print('查询结果为   D')
elif 0<=grade<60:
    print('查询结果为   E')
else:
    print('成绩有误，请输入0-100以内整数')


```
