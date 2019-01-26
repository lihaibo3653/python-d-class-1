class ClassName():

    def __init__(self,values = None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return iter(self.values)

    def __setitem__(self, key, value):
        if len(self.values) > key:
            self.values[key] = value

    def __getattr__(self, key):
        return self.values[key]

    def __str__(self):
        s = ''
        for v in self.values:
            s += str(v)
        return s

    def __delitem__(self, key):
        del self.values[key]

c = ClassName(values=[2,3,4,5,6])
print(len(c))
c[0] = 0
c[1] = 1

del c[1]
for v in c:
    print(v)

print(str(c))