```py


# ---------------trying-----------------
# 时间2021/8/22 20:30
'''a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break#直接结束循环，跳过后续步骤和while并列的else
    print('密码错误')
    a+=1
else:
    print('对不起，三次输入机会以用完')'''
a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1
else:
    print('对不起，三次密码均输入错误')

```
