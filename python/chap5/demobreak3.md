```py
# ---------------trying-----------------
# 时间2021/8/23 15:54
'''流程控制语句break与ontinue在二重循环中的使用'''
for i in range(5):  #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()

```
