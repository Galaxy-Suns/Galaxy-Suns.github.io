# ---------------trying-----------------
# 时间2021/8/20 17:37
'''会员 >=200 打八折
       >=100 打九折
             不打折
   非会员
       》=200 打九五折
             不打折'''
answer=input('您是会员吗？y/n')
money=float(input('购物金额'))
#外层判断
if answer=='y':#会员
    print('会员')
    if money>=200:
        print('打8折，付款金额为',money*0.8)
    elif money>=100:
        print('打9折，付款金额为',money*0.9)
    else:
         print('不打折，付款金额为',money)
else:          #非会员
    print('非会员')
    if money>=200:
        print('打9.5折，付款金额为',money*0.95)
    else:
        print('不打折，付款金额为',money)

