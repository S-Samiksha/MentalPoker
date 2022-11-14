# Derived from https://realpython.com/python-sockets/#echo-client-and-server

import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from Bob_func import *
import Deck 

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~ Bob ready to play ~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 53140  # Port to listen on (non-privileged ports are > 1023)
while (True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                print()
                print("~~~~~~~~~~~~~~~~~~~ Bob Receiving Deck~~~~~~~~~~~~~~~~~~~~~~~~")
                data = conn.recv(40000)
                if not data:
                    break
                #Send/Receiving cards ----------------
                data_alice = data.decode()
                print("Recived from Alice: ", data_alice)

                temp1 = data_alice.replace("'", "")
                print(temp1)
                temp = temp1.strip("']['").split(', ')
                print(temp)
                
                cardDeckReceived = Deck.Deck(temp)
                print("Initialized Deck: ", cardDeckReceived.getDeck())

                print("~~~~~~~~~~~~~~~~~~~ Bob Selects 5 for Alice ~~~~~~~~~~~~~~~~~~")
                AliceCardsA = cardDeckReceived.pickCards()
                print("Alice cards (a): ", AliceCardsA)

                conn.sendall(str(AliceCardsA).encode())

                print("~~~~~~~~~~~~~~~~~~~ Bob Selects 5 for himself ~~~~~~~~~~~~~~~~~~")
                BobCardsA = cardDeckReceived.pickCards()

                BobCardsAB =[]
                for value in BobCardsA:
                    BobCardsAB.append(bob_encrypt_alice(value))
                
                print(BobCardsAB)
                conn.sendall(str(BobCardsAB).encode())

                data_B = conn.recv(4096)

                print("~~~~~~~~~~~~~~~~~~~~Bob Decrypts for himself~~~~~~~~~~~~~")
                data_Bob = data_B.decode()
                temp1 = data_Bob.replace("'", "")
                temp = temp1.strip('][').split(',')
                print(temp)

                results = []

                for value in temp:
                    results.append(bob_decrypt(value))

                print("Bob's hand is : ", results)

                break

                



