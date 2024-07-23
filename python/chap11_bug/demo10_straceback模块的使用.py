'''10 straceback 模块的使用'''

#print(10/0)
import traceback
try:
    print('----------------------------')
    print(7/0)
except ZeroDivisionError :
    print(1)
    traceback.print_exc()