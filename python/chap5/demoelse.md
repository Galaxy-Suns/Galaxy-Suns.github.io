```py
# ---------------trying-----------------
# 时间2021/8/22 20:17
for item in range(3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:  #循环正常结束才会执行，而不是被 break 打断结束
    print('对不起，，三次密码均使用错误')```
