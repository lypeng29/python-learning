# def s(r):
#     return 3.14*pow(r,2)
# print(s(2))

# n1 = 255
# n2 = 1000
# print(hex(n1),hex(n2),hex(n2),hex(n2),hex(n2),hex(n2))


import math
def quadratic(a,b,c):
    # if not isinstance(a, (int, float)):
    #     raise TypeError('bad data type')
    if a==0:
        return 'a不能等于0'
    dt=pow(b,2)-4*a*c
    if dt>0:
        x=(-b+math.sqrt(dt))/(2*a)
        y=(-b-math.sqrt(dt))/(2*a)
        return ('方程组有两个解，分别为：x1=%.1f，x2=%.1f' %(x,y))
    elif dt==0:
        x=(-b+math.sqrt(dt))/(2*a)
        return ('方程组有一个解：x1=x2=%.1f' % x)
    else:
        return '方程组无解'
a=float(input('请输入a：'))
b=float(input('请输入b：'))
c=float(input('请输入c：'))
x=quadratic(a,b,c)
# if isinstance(x, (float, int)):
#     print('x1=x2=',x)
# elif isinstance(x, tuple):
#     print('x1=',x.x)
#     print('x2=',x.y)
# else isinstance(x, str):
print(x)


# def power(x,n):
#     s=1
#     while n>0:
#         s=s*x
#         n-=1
#     return s
# print(power(2,3))

'''
# *表示参数个数任意
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3,4))
'''

'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(len(str(fact(1000))))
'''

'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(len(str(fact(100))))
'''