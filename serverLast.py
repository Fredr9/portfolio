#!/usr/bin python3

import socket
import sys
import threading
import chatbots
import pickle

'''
HOST = 'localhost'
PORT = 1990
BOT = str(sys.argv[0])
'''

try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except (IndexError, ValueError):
    print("IP AND PORT MUST BE SPECIFIED! E.G serverLast.py localhost 1990")
    sys.exit()

SERVER_S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER_S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SERVER_S.bind((HOST, PORT))
SERVER_S.listen()
#threads = []

serverName = chatbots.Person("Server:")

clients = {}

print("Fredriks server is running!")


def broadcast(sender, message):
    for cli in clients:
        data = pickle.dumps((sender, message))
        cli.send(data)


def listen_data(cli):
    while True:
        try:
            sender, message = pickle.loads(cli.recv(2048))
            if not do_command(cli, message) and len(message) > 0:
                print(f"{sender.name}: {message}")
                broadcast(sender, message)
        except ConnectionResetError:
            p = clients.pop(cli, chatbots.ChatBot("Nobody"))
            print(f"{p.name} left")
            broadcast(chatbots.Person("server"), f"{p.name} left the chat!")
            cli.close()
            break
        except ConnectionAbortedError:
            break


def input_from_host():
    while True:
        message = input("")
        if not do_command(HOST, message) and len(message) > 0:
            broadcast(HOST, message)


hostThread = threading.Thread(target=input_from_host, daemon=True).start()


def do_command(client, message):
    commando = message.split(" ")
    if commando[0] in commandos:
        argument = " ".join(map(str, commando[1:]))
        commandos[commando[0]](client, argument)
        return True
    return False
'''
def name_update(client, name_new):
    if client == HOST:
        print("You need to be remained named as \"Host\"")
    else
        broadcast(chatbots.ChatBot("Server"), f"{clients[client].name}")

'''
commandos = {

}

while True:
    try:
        client, (HOST, PORT) = SERVER_S.accept()
    except OSError:
        print("Down with the server")
        break

    chatBotInvolved = pickle.loads(client.recv(1024))
    print(f"{HOST}:{PORT} joined as {chatBotInvolved.name}")

    clients.update({client: chatBotInvolved})
    client_thread = threading.Thread(target=listen_data, args=(client,)).start()
    broadcast(chatbots.Person("server"), f"{chatBotInvolved.name} Joined")

