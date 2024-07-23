'''字符串判断相关方法'''
s='hello,python'
print('1.',s.isidentifier()) #False 判断是否合法字符串：字母(汉字)数字下划线。
print('2.','hello'.isidentifier()) #True
print('3.','张三_'.isidentifier()) #True
print('4.','张三_123'.isidentifier()) #True

print('5.',' '.isspace()) #True 判断是否为空白字符：水平制表\t，回车，换行，空格

print('6.','abc'.isalpha()) #True 判断字符串是否全由字母（汉字）组成
print('7.','张三'.isalpha()) #True
print('8.','张三1'.isalpha()) #False

print('9.','123'.isdecimal()) #True 判断字符串是否全由十进制数字组成
print('10.','123四'.isdecimal()) #False
print('11.','ⅡⅡⅡ'.isdecimal()) #False

print('12.','123'.isnumeric()) #True 判断字符串是否全由数字组成
print('13','123四'.isnumeric()) #True
print('14.','ⅡⅡⅡ'.isnumeric()) #True

print('15.','abc1'.isalnum()) #True 判断字符串是否全由字母（汉字）和数字组成
print('16.','张三123'.isalnum()) #True
print('17.','abc!'.isalnum()) #False