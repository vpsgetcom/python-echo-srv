# !/usr/bin/env python

import socket

host = '0.0.0.0'
data_payload = 2048
backlog = 5
port = 4444


def echo_server(port):
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()
        data = client.recv(data_payload)

        #NOTED IT READING TASK ONCE AGAIN...
        if 'index.html' in data.decode():
        #if data == b'/index.html':
            print("Data is INDEX.HTML: %s" % data)
            print("sending back index.html content")

            f = open('index.html', 'rb')
            print('init send...')
            l = f.read(data_payload)
            while (l):
                print('Sending...')
                client.send(l)
                l = f.read(data_payload)
            f.close()
            print("Done Sending")
            print("sent %s bytes back to %s" % (data, address))
            print("client.close()")
            client.close()
        #just echo back string (bytes arrray)
        elif data:
            print("Data is %s" % data)
            # client.send(data)
            additionalMsg = "   || Server local IP : " + address[0]
            client.sendall(data + additionalMsg.encode())
            print("sent %s bytes back to %s" % (data, address))

        # end connection
        print("client.close()")
        client.close()

def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
    except:
        print("Unable to get Hostname and IP")

if __name__ == '__main__':
    get_Host_name_IP()
    echo_server(port)
