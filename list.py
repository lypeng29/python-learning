# -*- coding: utf-8 -*-
# 5.序列
# 序列定义
#x = ['1','2','3','4','5'];

# 序列调用
#x[0],x[0:],x[1:2],x[0:-1],x[-3:]
#x[0:3:2] x[1:3:2]

# 赋值，修改序列多个元素的值
# x[0:1]=[3]
# x[::2]=[99,99,99] #12345将变为： [99,2,99,4,99]

# 一些运算
#sum(x) min max len 

# 其他方法
# x.index('3')#第一次出现的下标
# x.count('3')#出现次数

#del x[0] #删除
#x.remove(3)
#x.clear()
#x.append([7,8]) #只能传一个参数，不能写成7,8，必须加[]
#x.extend([9,10]) #只能传一个参数
#x.insert(0,99) #insert(index,value)

#tuple
#不可变的序列（）

#l=('li','zhang','liu');

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

