
l = [1,1,2]

print(l)

a = set(['1','2','3'])

b = set(['1','4','5'])

print(a & b)

print(a | b)

print(a - b)


print(list(set(l)))


new_list = []
def remove_duplicate(l):
    for x in l:
        if x not in new_list:
            new_list.append(x)
    return new_list

remove_duplicate(l)

print(new_list)