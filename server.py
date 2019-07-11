import sys
import socket

def soc_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 8080
        s = socket.socket()
    except socket.error as msg:
        print("Failed to create the socket:"+str(msg))
        soc_bind()


def soc_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port:"+str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding failed"+str(msg)+"retrying.....")
        socket.bind()


def soc_accept():
    conn, address = s.accept()
    print("Ip add="+address[0],"\t"+"Port="+str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(1024),"utf-8")
                print(client_response,end="")



def main():
    soc_create()
    soc_bind()
    soc_accept()


main()