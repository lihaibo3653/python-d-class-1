d = dict()

def add(name,value):
    d[name] = value


def get(name):
    return d.get(name,None)

add('bee','蜜蜂; （集工作、竞赛、娱乐为一体的） 聚会')

print(get('bee'))

# get的时间复杂度是多少？O(1)

# 用数组(list)实现以上功能

l = []

def add(name,value):
    is_find = False
    for i in range(len(l)):
        if l[i][0] == name:
            l[i] = (name,value)
            is_find = True
            break
    if not is_find:
        l.append((name,value))

def get(name):
    for i in range(len(l)):
        if l[i][0] == name:
            return l[i][1]





add('bee','蜜蜂; （集工作、竞赛、娱乐为一体的） 聚会')
add('bee','蜜蜂;')

print(get('bee'))