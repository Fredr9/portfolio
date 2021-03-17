import socket
import re
import threading
import sys
import chatbots
import pickle

bots_available = {
    'hanne': chatbots.Hanne(),
    'jon': chatbots.Jon(),
    'joakim': chatbots.Joakim()
}

try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])

except(IndexError, ValueError):
    print("You must specify IP and PORT! E.G clientLast.py localhost 1990 Botname")
    sys.exit()

try:
    chatBotInvolved = \
        bots_available[sys.argv[3].lower()] \
            if len(sys.argv) == 4 \
            else chatbots.Person("Disconnect and choose a Botname! Jon or Hanne")
except KeyError:
    print(f"You have not chosen an available chatbot instead try one of these: \n"
          f"{list(bots_available.keys())}")
    sys.exit()
'''
if isinstance(chatboters, chatbots.Hanne):
    who = chatboters.ACTIONS['who']
    identify = chatboters.ACTIONS['identify']
    '''

client_s = socket.socket()
try:
    client_s.connect((IP, PORT))
except ConnectionRefusedError:
    print(f"Cannot connect with server at {IP}:{PORT}")
    sys.exit()

client_s.send(pickle.dumps(chatBotInvolved))


def data_receuve():
    while True:
        try:
            sender, message = pickle.loads(client_s.recv(1024))

            if sender.name == "server":
                print(f"{message}")
            elif sender.name != chatBotInvolved.name:
                print(f"{sender.name}: {message}")

        #    if isinstance(chatBotInvolved, chatbots.ChatBot) and isinstance(sender, chatbots.Person):
        #       respon = chatbots.respon_to(message)
        #      print(f"{chatBotInvolved.name}: {respon}")
        #     data = pickle.dumps((chatBotInvolved, respon))
        #    client_s.send(data)

            if isinstance(chatBotInvolved, chatbots.ChatBot) and isinstance(sender, chatbots.Person):
                response = chatBotInvolved.respond(message)
                print(f"{chatBotInvolved.name}: {response}")
                data = pickle.dumps((chatBotInvolved, response))
                client_s.send(data)

        except (ConnectionResetError, OSError, EOFError):
            print("Disconnectet from server")
            client_s.close()
            break


def send_data():
    while True:
        try:
            client_s.send(pickle.dumps((chatBotInvolved, "")))

            message = re.sub("[ ]", " ", input().strip())

        except (ConnectionAbortedError, EOFError, OSError):
            print(" COnnection not established")
            client_s.close()
            break


threading.Thread(target=data_receuve).start()

if isinstance(chatBotInvolved, chatbots.Person):
    threading.Thread(target=send_data, daemon=True).start()

sys.exit()
