#!/usr/bin

import socket
import select
import sys
import random

#if len(sys.argv) < 3:
#    print("Usage :  python {0} hostname port".format(sys.argv[0]))
#    sys.exit()

host = '' #sys.argv[1]
port = 1990 #int(sys.argv[2])
#bot = input()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.settimeout(200)

try:
    socket.connect((host, port))
except Exception as msg:
    print(type(msg).__name__)
    print("Cannot connect")
    sys.exit()

print("Connected to host. Start sending messages")

while True:
    SOCKET_LIST = [sys.stdin, socket]
    READ_SOCKETS, WRITE_SOCKETS, ERROR_SOCKETS = select.select(SOCKET_LIST, [], [])

    for sock in READ_SOCKETS:
        if sock == socket:
            data = sock.recv(8192)
            if not data:
                print('\n Disconnected from server')
                sys.exit()
            else:
                print("Nå fikk jeg en melding")
                print(data.decode(), end="")
        else:
            msg = sys.stdin.readline()
            print("\x1b[1A" + "\x1b[2k", end="")
            print("Nå sendes meldingen til server")
            socket.sendall(msg.encode())
