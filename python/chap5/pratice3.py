# ---------------trying-----------------
# 时间2021/8/22 21:52
#画一个9*9的直角三角形
for i in range(0,9):   #几行
    for j in range(0,9):  #每一行几列
        if i==j-1:
            break
        else:
            print('*',end='\t')
    print('')