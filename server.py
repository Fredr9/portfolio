#!/usr/bin python3

import socket
import select
import random
import sys
from threading import Thread
from socketserver import ThreadingMixIn

bots = ("Jon", "Frank", "Hanne", "Joakim")
test = random.choices(bots)

TCP_IP = '0.0.0.0'
TCP_PORT = 2021
BUFFER_SIZE = 1024


def broadcast_message(message):
    """ Sends message to every sockets in the connection list."""

    for sockets in CONNECTION_LIST:
        if sockets != SERVER_S:
            try:
                print("Etter Try")
                print("Lengeden på CONNECTION_LIST ER " + str(len(CONNECTION_LIST)))
                sockets.sendall(message)
            except Exception as msg:
                print(type(msg).__name__)
                print("Er det her da=")
                sockets.close()
                try:
                    print("er dette der det er feiLOI")
                    CONNECTION_LIST.remove(sockets)
                except ValueError as msg:
                    print("{}:{}".format(type(msg).__name__, msg))


CONNECTION_LIST = []
RECV_BUFFER = 4096
HOST = 'localhost'
PORT = 1990
BOT = str(sys.argv[0])

SERVER_S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SERVER_S.bind((HOST, PORT))
threads = []
'''
print("Listening..")
SERVER_S.listen(4)
'''
CONNECTION_LIST.append(SERVER_S)
print("Fredriks Server has started!")

while True:

    print("Listening..")
    SERVER_S.listen(4)
    READ_SOCKETS, WRITE_SOCKETS, ERROR_SOCKETS = select.select(CONNECTION_LIST, [], [])
    for SOCK in READ_SOCKETS:
        if SOCK == SERVER_S:

            SOCKFD, ADDR = SERVER_S.accept()
            CONNECTION_LIST.append(SOCKFD)

            if len(CONNECTION_LIST) == 3:
                print("Nå er alle tilkoblet PARTY")
                print("Lengeden på CONNECTION_LIST ER " + str(len(CONNECTION_LIST)))
                broadcast_message("FÅR ALLE MELDINGEN?".encode())
            print("\r Chatbot ({0}, {1} connected!".format(ADDR[0], ADDR[1]))

            broadcast_message("Client ({0}:{1}) entered the room \n"
                              .format(ADDR[0], ADDR[1]).encode())

        else:
            try:
                print("Her venter jeg på en melding")
                DATA = SOCK.recv(RECV_BUFFER)

                print("Nå skal meldingen ha kommet " + DATA.decode())
                continue
                if DATA:
                    ADDR = SOCK.getpeername()

                    message = "\r[{}:{}]: {}".format(ADDR[0], ADDR[1], DATA.decode())
                    print(message, end="")
                    broadcast_message(message.encode())

            except Exception as msg:
                print(type(msg).__name__, msg)
                print("\rChatbot ({0}, {1} is disconnected \n".format(ADDR[0], ADDR[1]))
                broadcast_message("\r Chatbot ({0}, {1} is offline)\n"
                                  .format(ADDR[0], ADDR[1]).encode())
                SOCK.close()
            # try:
            #   print("Nå fjerner jeg socket")
            # CONNECTION_LIST.remove(SOCK)
            # except ValueError as msg:
            #   print("{}:{}".format(type(msg).__name__, msg))
            continue

            SERVER_S.close()
