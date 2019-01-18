
string = "123456789"
string = '123456789'


print(string[0])
print(string[2])

print(string * 2)
print(string[1:4])

if '3' in string:
    print('3存在于字符串中')
if 'a' not in string:
    print('a 不存在于字符串中')

print("'a'")
# 'a'
print('\'a\'')
# 'a'
print("\"a\"")

print(len(string))
print(string.find("345"))
print(string.replace("1","a"))

a = "abc"
A = "ABC"

print(A.lower())
print(a.upper())

s = string.replace("2","b")
print(s)

