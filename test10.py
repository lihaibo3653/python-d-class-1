
l = [1,"1","a",1.0]

print(l[0])
print(l[1])

print(len(l))

print(l[3])

l.append("c")
print(l)

l.insert(0,"c")
print(l)

del l[0]
print(l)

arrays = [[1,2,3],[4,5,6]]

for a in arrays:
    for x in a:
        print(x)

