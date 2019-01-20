
d = {
    'key':'value',
    'key1':'value1',
    'key2':1.0
}

print(d)

print(d['key1'])

#修改
d['key1'] = 'new value1'
#新增
d['key3'] = 'value3'

print(d)

#删除

del d['key3']
print(d)


for k in d:
    print(k)
    v = d[k]
    print(v)


