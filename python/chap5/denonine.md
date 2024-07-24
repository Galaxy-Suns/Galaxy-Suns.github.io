```py


# ---------------trying-----------------
# 时间2021/8/22 22:13
for i in range(1,10):   #行数
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end=' ')
    print()
fp=open('D:/lesson.txt','a+')
print('''改p45二重循环了
2021/8/22
22:28''',file=fp)
fp.close


```
