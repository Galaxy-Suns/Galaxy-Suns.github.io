# ---------------trying-----------------
# 时间2021/8/20 12:00
#序号输入模块-------------------------------------------------------------------------------------
a='0'
b=0
while b==0:
    for item in range(1,11):
        if a==str(item) and a!='10':
            b=1
            break
        if item==10:
            print('对不起，输入无效，可以输入从1到9的序号')
        if item>1:
            continue
        a=input('请输入操作序号')
#------------------------------------------------------------------------------------------------
