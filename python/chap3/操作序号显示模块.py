# ---------------trying-----------------
# 时间2021/8/25 22:59
#操作序号显示模块------------------------------------------------------------
d=input('如需要查看操作序号，输入\'y\'并按下回车,跳过请直接按下回车')
print('')
while d!='y' and d!='':
    print('报错！仅可输入\'y\'或直接按下回车')
    print('')
    d=input('请重新输入')
    print('')
if d=='y':
    print('''操作序号y

    1.加法

    2.减法

    3.乘法

    4.除法

    5.幂运算

    6.开n次根号

    7.整除

    8.取余

    9.比大小''')
    print('')
#-------------------------------------------------------------操作序号显示模块