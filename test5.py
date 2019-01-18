a = 5
l = [1,2,3,4,5]
b = 6

if a in l:
    print('a 在l中')

if b not in l:
    print('b 不在l中')


if a is not b:
    print('a 跟 b 不是同一个对象')


a if print(a) else print(b)
# 为真的结果 if 判断的条件 else 为假的结果