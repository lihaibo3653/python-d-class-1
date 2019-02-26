import socket,threading,json
from network.message import send_auth,send_message,send_client_message
from network.DataHandler import DataHandler


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()

port = 9088

print('监听',port,'端口')

s.bind((host,port))
s.listen(5)

user_connections = dict()

client_methods = dict()

def client_method_message():
    pass

def client_method_auth():
    pass

client_methods['message'] = client_method_message
client_methods['auth'] = client_method_auth


def client_connection(c,addr):
    data_hanlder = DataHandler()
    local_connection_uid = None
    while True:
        try:
            data = c.recv(1024)
        except ConnectionResetError as error:
            print('客户端关闭:',addr)
        if data:
            #data = data.decode('utf-8')
            print('接收到客户的data:',data)
            data_hanlder.push(data)
            for data in data_hanlder.get_datas():
                client_message_object = (data)
                print(addr,'客户端发来的数据:',client_message_object)
                a = client_message_object.get('a',None)
                client_method = client_methods.get(a,None)
                if client_method:
                    client_method()
                if a == 'heartbeat':
                    print('接收到心跳包：',addr)
                if a == 'message':
                    #处理用户消息转发
                    to_uid = client_message_object['to_uid']
                    user_connection = user_connections.get(to_uid,None)
                    if not user_connection:
                        print('用户不在线.')
                    else:
                        message = client_message_object['message']
                        send_client_message(s = user_connection,message=message,from_uid = local_connection_uid)
                elif a == 'auth':
                    #处理用户验证
                    username = client_message_object['username']
                    if username:
                        print('验证用户[',username,']','成功。')
                        user_connections[username] = c
                        local_connection_uid = username
                    else:
                        print('验证不通过')

        else:
            print('客户端关闭')
            break

while True:
    c,addr = s.accept()
    print('有新的客户端连接:',addr)
    t = threading.Thread(target=client_connection,args=(c,addr))
    t.start()

print('服务器运行结束')
