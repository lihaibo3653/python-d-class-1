
def functionname(parameters):
    #函数的实现
    return parameters #任何类型的值

ret = functionname(10)
print(ret)


def printperson(name,age,gender = 'unknown',*args,**kwargs):
    print('name:',name)
    print('age:',age)
    print('gender:',gender)
    print('args:',args)
    print('kwargs:',kwargs)
    print('\n')
    return name,age


printperson(name = 'lihaibo',age = 29)
printperson(name = 'lihaibo',age = 29,gender='male')

printperson('lihaibo',29)
printperson('lihaibo',29,'male')


printperson('lihaibo',29,"male",'ShangHai',"iotek")
name = printperson('lihaibo',29,location = "ShangHai",company = "iotek")
print('name:',name)

