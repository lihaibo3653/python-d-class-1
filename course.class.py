class Person(object):

    __slots__ = ('name',)

    def __init__(self,name,age = 29,gender = 'male'):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def print_info(self):
        print('name',self.__name,' age:',self.__age,' gender:',self.__gender)
        #return None

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

'''c = Person('class name',29,'male')
print('c:',c)
c.name = 'name'
c.age = 29
c.print_info()
c.set_name('lihaibo')
print(c.get_name())'''

class SuperPerson(Person):
    __slots__ = ('name',)

sp = SuperPerson('1222',27)
sp.print_info()

#创建一个类，传入你们的基本信息包括 名字，年龄，性别

'''uers = {
    'username':{
        'password':'12345678'
    }
    ,
    'username1':{
        'password':'12345678'
    }
}

def login(username,password):
    userinfo = uers.get(username)
    if userinfo.get('password') != password:
        return '用户名或密码错误'
        
'''
import os

class File():


    def __init__(self,file_path):
        self.__file_path = file_path
        self.open()

    def open(self):
        self.__file_handler = open(self.__file_path,'r')
        self.__file_content  = self.__file_handler.read()

    def __del__(self):
        print('file del method call:',self)
        if self.__file_handler:
            self.__file_handler.close()

    def get_file_path(self):
        return self.__file_path

    def get_file_size(self):
        return os.path.getsize(self.__file_path)

    def get_create_time(self):
        return os.path.getctime(self.__file_path)

    def get_modify_time(self):
        return os.path.getmtime(self.__file_path)

    def get_owner(self):
        pass

    def move(self,dst):
        pass

    #实现remove方法
    def remove(self):
        if os.path.isfile(self.__file_path):
            self.__file_handler.close()
            os.remove(self.__file_path)
            self.__file_handler = None


    def read(self,*args):
        return self.__file_content

    def write(self,*args):
        pass

    def copy(self,dst):
        f = open(dst,'w')
        f.write(self.read())
        f.close()



class Script(File):

    def execute(self):
        pass

class Python(Script):
    pass

class Video(File):

    def play(self):
        pass

class Image(File):

    def open(self):
        self.__file_handler = open(self.get_file_path(),'rb')
        self.__file_content  = self.__file_handler.read()

    def show(self):
        pass

image = Image('images/111.png')
print(isinstance(image,Image))
print(isinstance(image,File))
print(isinstance(image,Video))
