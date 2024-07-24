```py


# ---------------trying-----------------
# 时间2021/8/22 1:05
'''输出100到999之间的水仙花数
   举例：
   153=3*3*3+5*5*5+1*1*1
'''
'''for a in range(1,10):
    for b in range(0,10):
        for c in range(0, 10):
            if 100*a+10*b+c==a**3+b**3+c**3:
                print(100*a+10*b+c)'''

for item in range(100,1000):
    ge=item%10       #个位
    shi=item//10%10  #十位
    bai=item//100    #百位
    #print(ge,shi,bai)
    if ge**3+shi**3+bai**3==item:
        print(item)
fp=open('D:/lesson.txt','a+')
print('''改P40流程控制语句break了
2021/8/22
1:27''',file=fp)
fp.close

```
