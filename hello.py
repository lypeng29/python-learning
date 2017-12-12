#!/usr/bin/python3
# 1.hello world
# print('hello world!');

# 2.keyword
# import keyword;
# print(keyword.kwlist); #保留关键字
"""多行注释
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

# 3.缩进一致,不存在运行错误，但还是注意吧
#if 5>3:
#    print('true');
#else
#   print('false');
#print('55');

# 4.'''多行字符串
#things = '''this is a p
#duo hang zi fu chuan''';
#print(things);

print(ord('A'))

print(chr(65))

lastf = float(input('your last year fenshu: '))
yearf = float(input('your jin year fen : '))
bfb = (yearf-lastf)/yearf*100
print("去年成绩：%.2f,今年成绩：%.2f,提升百分比为：%.2f%%" % (lastf,yearf,bfb))
# print('%')