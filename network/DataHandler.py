import struct,json

d = struct.pack('H',1234)
l = struct.unpack('H',d)
print(l)
'''

# 代表一个字节

##(后续包的长度)包的内容

'''


class DataHandler():

    def __init__(self):
        self.data = b''
        self.datas = []

    def push(self,data):
        self.data += data
        self.update()

    def first_data_len(self):
        if len(self.data) > 2:
            l_byte = self.data[0:2]
            l = struct.unpack("H",l_byte)
            l = l[0]
            return l


    def get_datas(self):
        while len(self.datas) > 0:
            yield self.datas.pop(0)

    def update(self):

        l = self.first_data_len()

        while self.data and len(self.data) >= l + 2:
            data_byte = self.data[2:l + 2 ]
            print(data_byte)
            data = data_byte.decode('utf-8')
            print('data:',data)
            data = json.loads(data)
            self.datas.append(data)
            self.data = self.data[l+2:]

            l = self.first_data_len()

