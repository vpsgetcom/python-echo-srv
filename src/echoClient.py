#!/usr/bin/env python3

import socket

HOST = 'localhost'
PORT = 4444
data_payload = 2048

#TEST1 : send msg and expect to receive this msg as reply
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print ("sending test string ... ")
    s.sendall(b'This is a test message that should be echoed ... Hey! echo me!')
    data = s.recv(data_payload)
    print('Received', repr(data))
    s.shutdown(socket.SHUT_WR)

#TEST2 : send specific and expect to receive file content  as reply
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("sending /index.html..we need to get back content of index.html (or we need to server it with python simple hhtp server?) ... ")
    s.connect((HOST, PORT))
    s.sendall(b'/index.html')

    print("Receiving...")
    l = s.recv(data_payload)
    while (l):
        #print("Receiving...")
        #f.write(l)
        print(l)
        l = s.recv(data_payload)
    s.shutdown(socket.SHUT_WR)
    s.close()
    print("DONE")



