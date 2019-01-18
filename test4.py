
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a**b)
print(a % b)
print(b // a)

print('比较运算符')
print('\n')

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


print('赋值运算符')
print('\n')

a = 5
b = 2

a += 1
#a = a + 1

a -= 1
# a = a - 1

a *= 2

a **= 2

a /= 2

a %= 2

a //= 2


print('位运算符')
print('\n')

a = 5
b = 1

print('a的二进制:',bin(a),'b的二进制:',bin(b))

print((a & b))
print((a | b))
print((a^b))
print((~a))
print((a<<2))
print((a>>2))


print('逻辑运算符')
print('\n')

print(a and b)
print(a or 2)
print(not a)