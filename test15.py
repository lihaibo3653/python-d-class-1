l = [0,1,2,3,4,5,6,7,8,9]

[l[0],l[1]]

print(l[0:2])
print(l[0:8:2])


def cut_list(l,start,end,step = 1):
    new_l = []
    for i in l:
        if i >= start and i < end:
            new_l.append(i)
    return new_l

print(cut_list(l,0,2))


print(l[-1])
print(l[:-1])



#10
print(list(range(len(l))))
print(l[-2:-1])

def cut_list(l,start,end,step = 1):
    new_l = []
    if start > 0 or end > 0 or start > end:
        return new_l
    l_len = len(l)
    s = l_len + start
    e = l_len + end
    for i in range(len(l)):
        v = l[i]
        if i >= s and i < e:
            new_l.append(l[i])
    return new_l

print(cut_list(l,start = -2,end = -1))


for i in [2,6,8]:
    print(i)

#0，1，2


for x in "ABC":
    pass

for i in l:
    pass

d = {'a':1,'b':2,'c':3}
for k in d:
    print(k)

for i,v in enumerate([3,5,8,0]):
    print('i:',i,' v:',v)

for x,y in [(2,2),(4,4),(9,9)]:
    print(x,y)

num_l = [10,20,40,33,9,200,36]

print(max(num_l))

def max_num(l):
    x = num_l[0]
    y = num_l[0]
    for v in num_l:
        if x < v:
            x = v
        if y > v:
            y = v
    return x,y

print(max_num(num_l))

#获取最大值和最小值 并返回（max,min）

