import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("You need to use: script, IP, PORT")
    exit()

IP = str(sys.argv[1])
PORT = int(sys.argv[2])
server.connect((IP, PORT))

while True:

    sockets_list = [sys.stdin, server]
    read_sockets, write_sockets, error_sockets = select.select(sockets_list,[],[])

    for sockets in read_sockets:
        if sockets == server:
            message = sockets.recv(1024)
            print(message)
        else:
            message = sys.stdin.readline()
            server.send(message.format().encode())
            sys.stdout.write("<YOU>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
