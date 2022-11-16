# Derived from https://realpython.com/python-sockets/#echo-client-and-server

import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import Deck 
import Hand
import Data
import Winner
import key

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Bob ready to play~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



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
                bob_key = key.key()


                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                                      Receiving Deck                                      ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                data = conn.recv(40000)
                if not data:
                    break

                data_alice = Data.decode(data)
                print("Received: ", data_alice)
                cardDeckReceived = Deck.Deck(data_alice)

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                        Selecting 5 Cards for Alice + Sending to Her                      ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                aliceCardsA = cardDeckReceived.pickCards()

                conn.sendall(str(aliceCardsA).encode())

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                                   Selecting Own 5 Cards                                  ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
                bobCardsA = cardDeckReceived.pickCards()

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                           Encrypting Own Cards + Sending to Alice                        ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                bobCardsAB =[]
                for value in bobCardsA:
                    bobCardsAB.append(bob_key.bob_alice_encrypt(value))
                print("Encrypted cards: ",bobCardsAB)

                conn.sendall(str(bobCardsAB).encode())

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                                   Receiving Own Cards                                    ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                data = conn.recv(4096)
                data_alice = Data.decode(data)
                print("Received: ", data_alice)

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                    Decrypting Cards to Get Own Hand + Sending Own Hand                   ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                bobCards = []
                for value in data_alice:
                    bobCards.append(bob_key.card_decrypt(value))
                bobHand = Hand.Hand(bobCards)
                print("Bob's hand is : ", bobCards)
                print(bobHand.getHand())

                conn.sendall(str(bobCards).encode())

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                                 Receiving Alice's Hand                                   ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                data = conn.recv(4096)
                aliceCards = Data.decode(data)
                aliceHand = Hand.Hand(aliceCards)
                print("Received: ", aliceCards)
                print("Alice's's hand is : ", aliceHand.getHand())

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                                  Results of the Game                                     ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
                winner = Winner.Winner(aliceCards,bobCards).getWinner()
                if (winner == 1):
                    print("Alice wins !!")
                else:
                    print("Bob wins!!")

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                                      Check Cheating                                      ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                
                e_key, d_key = bob_key.return_keys()
                alice_e_key = conn.recv(1024)
                conn.sendall(str(e_key).encode())
                print("Alice's Encryption Key is: ", alice_e_key.decode())
                alice_d_key = conn.recv(1024)
                conn.sendall(str(d_key).encode())
                print("Alice's Decryption Key is : ", alice_d_key.decode())

                #Decrypt Alice's hand 
                results = []
                for value in aliceCardsA:
                    results.append(bob_key.decrypt_other(value, alice_d_key.decode()))
                print(results) # Alice's decrypted hand in terms of numbers not the 'ace of hearts' kind

                AlicesHand = Hand.Hand(results)
                print(AlicesHand.getHand())

                #Now I check if what i receive from alice is the same as what bob sent earlier to alice
                if (AlicesHand.getHand()==aliceHand.getHand()):
                    print("There has been no cheating!")
                else:
                    print("There has been cheating!!!!")


                break
                conn.close()
    break
                

                



