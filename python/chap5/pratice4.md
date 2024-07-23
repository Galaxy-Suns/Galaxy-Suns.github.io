```py
# ---------------trying-----------------
# 时间2021/8/22 22:10
#输出九九乘法表
for i in range(1,10):   #几行
    for j in range(1,10):  #每一行几列
        if i==j-1:
            break
        else:
            print(str(i)+'×'+str(j)+'='+str(i*j),end='\t')
    print('')```
