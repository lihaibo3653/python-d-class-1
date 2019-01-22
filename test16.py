[0 * 0,1 * 1 , ]

l = []

for x in range(11):
    l.append(x * x)

print(l)

l = [x * x for x in range(11)]
print(l)

l = [x * x for x in range(11) if x % 2 == 0]
print(l)

#只有奇数的数组

"ABC" "XYZ"

print([a + b for a in "ABC" for b in "XYZ"])

"ABC" "XYZ" "123"

M = [[1,2,3],[4,5,6],[7,8,9]]
N = [[3,3,3],[4,4,4],[6,6,6]]

#numpy
print([M[row][col] * N[row][col] for row in range(len(M)) for col in range(len(N))])


d = {
    "k1":10,
    "k2":20,
    "k3":30
}
print({k:v + 10 for k,v in d.items()})
print({k:v for k,v in d.items() if v >= 20})
print({v:k for k,v in d.items()})
print({k:v + 10 if v <= 20 else v - 10 for k,v in d.items()})



l = [2,3,4,5,6]
s = { i * i for i in l }
print(s)

