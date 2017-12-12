'''
sg = float(input('your sg: '));
tz = float(input('your tz:'));
bmi=tz/(sg**2);
print('your bmi is : ',bmi);
if bmi < 18.5:
    print('guoqing')
elif (bmi >= 18.5 and bmi <25):
    print('normal')
elif (bmi >= 25 and bmi <28):
    print('guo zhong')
elif (bmi >= 28 and bmi <32):
    print('pang')
else:
    print('yanzhogn pang')
'''
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)
'''
sum=0;
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    sum += i;
print('sum is : ',sum);
'''
# x=list(range(10))
# print(x)
'''
sum=0
for i in range(101):
    sum += i
print('sum is : ',sum)
'''

'''
sum=i=0
while i<101:
    sum += i
    i+=1   #i++无效，+=可以
print(sum)
'''

# L = ['Bart', 'Lisa', 'Adam']
# for i in L:
#     print('HELLO ',i)

# n=1
# while n<=10:
#     n+=1
#     if n%2==1:
#         continue
#     print(n)
# print('end')

#dict字典，类似json,redis,key-value库
d={'zhang':80,'liu':90,'ma':85}
print(d['zhang'])

if 'tom' in d:
    print(True)
else:
    print(False)

# d.get('zhang')
# d.pop('zhang')

#set
# set list tuple 有些混乱了，暂且搁置，看下面的