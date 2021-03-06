import socket,json,struct


#发送聊天信息
def send_heartbeat(s:socket.socket,time):
    send_object = dict()
    send_object['a'] = 'heartbeat'
    send_object['time'] = time
    send_data = json.dumps(send_object)
    print('发送的消息:',send_object)
    send_data = send_data.encode('utf-8')
    send_pack(s,send_data)


def send_pack(s:socket.socket,send_data):
    l = len(send_data)
    send_bytes = struct.pack('H',l)
    send_bytes = send_bytes + send_data
    s.send(send_bytes)


def send_register(s,username,password,email):
    pass

#发送验证信息
def send_auth(s,username,password):
    send_object = dict()
    send_object['a'] = 'auth'
    send_object['username'] = username
    send_object['password'] = password
    send_data  = json.dumps(send_object)
    send_data = send_data.encode('utf-8')
    send_pack(s,send_data)

#发送聊天信息
def send_message(s:socket.socket,message,to_uid):
    send_object = dict()
    send_object['a'] = 'message'
    send_object['to_uid'] = to_uid
    send_object['message'] = message
    send_data = json.dumps(send_object)
    print('发送的消息:',send_object)
    send_data = send_data.encode('utf-8')
    send_pack(s,send_data)


def send_client_message(s:socket.socket,message,from_uid):
    send_object = dict()
    send_object['a'] = 'message'
    send_object['from_uid'] = from_uid
    send_object['message'] = message
    send_data = json.dumps(send_object)
    print('[send_client_message]发送的消息:',send_object)
    send_data = send_data.encode('utf-8')
    send_pack(s,send_data)
