```py


# ---------------trying-----------------
# 时间2021/8/13 22:32
q=5.6
w=4
e=3.1
r=2.1
y=6
u=14.99
i=1028
o=105
p=3
fp=open('D:/review.txt','a+')
print('牛奶\t\t\t\t',q,chr(20803),file=fp)
print('果冻\t\t\t\t',w,chr(20803),file=fp)
print('橡皮泥\t\t\t\t',e,chr(20803),file=fp)
print('香蕉\t\t\t\t',r,chr(20803),file=fp)
print('苹果\t\t\t\t',y,chr(20803),file=fp)
print('三文鱼\t\t\t\t',u,chr(20803),file=fp)
print('手镯\t\t\t\t',i,chr(20803),file=fp)
print('天平\t\t\t\t',o,chr(20803),file=fp)
print('圆珠笔\t\t\t\t',p,chr(20803),file=fp)
from decimal import Decimal
print('合计\t\t\t\t',Decimal('5.6')+Decimal('4')+Decimal('3.1')+Decimal('6')+Decimal('14.99')+Decimal('1028')+Decimal('105')+Decimal('3'),chr(20803),file=fp)
fp.close




```
