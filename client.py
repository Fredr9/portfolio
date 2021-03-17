#!/usr/bin

import socket
import select
import sys
import random

bots = "Jon", "Frank", "Hanne", "Joakim"


def bot(action, alt_action=None):
    return "I think {} sounds great!".format(action + "ing"), None


def jon(a, b=None):
    return "I think {} sounds fantastic!".format(a + "ing")


def frank(a, b=None):
    if b is None:
        return "Not sure about {}. Can i get a Choice?".format(a + "ing")
    return "Of course, both {} and {} seems ok to me".format(a, b + "ing")


def hanne(a, b=None):
    alternatives = ["walking", "talking", "swimming", "shopping"]
    b = random.choices(alternatives)
    res = "Yes, {} is a good options, but we can try some {}".format(a, b)
    return res, b


def joakim(a, b=None):
    action = a + "ing"
    bad_things = ["hitting", "screaming", "yelling", "complaining"]
    good_things = ["singing", "running", "working", "playing"]

    if action in bad_things:
        return "YESS! Its {} time!".format(action)
    elif action in good_things:
        return "Wait what!? this suggestion sucks, {} is not a good idea".format(action)
    return "I don't care!"


action = random.choice(["sing", "test", "box", "try", "talk"])

#print("\nMe: Do you guys wanna {}? \n".format(action))
#print("Jon: {}".format(jon(action)))
#print("Frank: {}".format(frank(action)))
#print("Hanne: {}".format(hanne(action)[0]))
#print("Joakim: {}".format(joakim(action)))


if len(sys.argv) != 4:
    print("You need to have script, host, port, bot")
    sys.exit()
else:
    bot_name = str(sys.argv[3])
    print(bot_name)
    if (bot_name) in ("Jon, Frank, Hanne, Joakim"):  # sys.argv[3]) == (["Jon", "Frank", "Hanne", "Joakim"]):
        print(" DU har nå logget inn!")
        print("\nMe: Do you guys wanna {}? \n".format(action))

    if (bot_name) not in ("Jon", "Frank", "Hanne", "Joakim"):
        print(" You have too write the name of one of the bots!")
        sys.exit()

    else:
        if (sys.argv[3]) == (["Jon", "Frank", "Hanne", "Joakim"]):
            print(" DU har nå logget inn!")
            print("\nMe: Do you guys wanna {}? \n".format(action))
        if (bot_name) == ("Jon"):
            print("Jon: {}".format(jon(action)))
        if (bot_name) == ("Frank"):
            print("Frank: {}".format(frank(action)))
        if (bot_name) == ("Hanne"):
            print("Hanne: {}".format(hanne(action)[0]))
        if (bot_name) == ("Joakim"):
            print("Joakim: {}".format(joakim(action)))



# if len(sys.argv) < 3:
#    print("Usage :  python {0} hostname port".format(sys.argv[0]))
#    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])
bot = sys.argv[3]

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.settimeout(200)

# botname = sys.argv[3]

# melding = "hallo"
# meldingTilServer = botname + ": " + melding

# socket.send(meldingTilServer.encode())

try:
    socket.connect((host, port))
#   socket.send(input())
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
