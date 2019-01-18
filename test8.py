c = 1 + 2 + 3
#1 加到 1000
# for
# while

sum = 0

for i in range(1000):
    if i == 100:
        #break
        continue
    sum += i



#break
#continue

print(sum)

for letter in 'Python':
    if letter == 't':
        continue
        #接下来的代码不会执行
        break
        #直接跳了循环语句
    print(letter)
    print('\n')

print('代码运行结束')