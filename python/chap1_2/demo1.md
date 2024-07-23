```py
# ---------------trying-----------------
# 时间2021/6/2613:54
#可以输出数字
print(520)
print(98.5)
#可以输出字符串（要加’‘或“”）
print('helloworld')
print("helloworld")
#含有运算符的表达式
print(3+1)

#将数据输出到文件中 注意点1.所指定的盘符存在2.使用file=fp
fp=open('D:/text.txt','a+')#a+的含义是如果文件不存在就创建，存在就在文件后面追加
print('helloworld',file=fp)
fp.close()
fp=open('D:/text1.txt','a+')
print('hello',file=fp)
fp.close()

#不进行换行输出（输出内容在一行当中）
print('hello','world','python')
```
