import socket,json,threading,time
from network.message import send_auth,send_message
from network.DataHandler import DataHandler

class Client():

    def __init__(self,username,password):
        self.auth = (username,password)
        self.connect_success = False
        self.data_handler = DataHandler()

    def connect(self,host = None,port = 9088):
        s = socket.socket()
        if host is None:
            host = socket.gethostname()

        s.connect((host, port))

        # print(s.recv(1024).decode('utf-8'))

        def server_connection(s: socket.socket):
            while True:
                data = s.recv(1024)
                self.data_handler.push(data)
                for data in self.data_handler.get_datas():
                    print('\n[{}]接收到服务器的数据:'.format(self.auth[0]), data)
                    message_object = (data)
                    if message_object['a'] == 'message':
                        print('[{}]说:{}'.format(message_object['from_uid'],message_object['message']))

        # 启动监听服务器消息的线程
        server_thread = threading.Thread(target=server_connection, args=(s,))
        server_thread.start()

        send_auth(s, *self.auth)

        '''while True:
            str = input('请输入:')
            send_message(s, message=str, to_uid='1001')'''

        self.connect_success = True
        self.connection = s

    def send_message(self,message,to_uid):
        if not self.connect_success:
            print('未建立与服务器的连接')
            return False
        send_message(s = self.connection,message=message,to_uid = to_uid)


t1 = Client('test','test')
t1.connect()

t2 = Client('test2','test')
t2.connect()


time.sleep(3)

t1.send_message(message='你好',to_uid='test2')
time.sleep(3)
t1.send_message(message='在吗?',to_uid='test2')
t1.send_message(message='在吗1?',to_uid='test2')
t1.send_message(message='在吗2?',to_uid='test2')


while True:
    import time
    time.sleep(1)
