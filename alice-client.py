# Derived from https://realpython.com/python-sockets/#echo-client-and-server
# Derived from https://medium.com/asecuritysite-when-bob-met-alice/bob-and-alice-play-mental-poker-in-a-world-where-they-trust-no-one-6cc557596169 

#Application usage for Alice

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
import time
import key

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Alice ready to play~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 53140  # The port used by the server

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        alice_key = key.key()

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                       Creating Deck                                      ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        cardDeck = Deck.Deck()
        deck = cardDeck.getDeck() #deck is a list 
        print("Deck is: ", deck)


        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                      Encrypting Deck                                     ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        encrypted_deck = []
        for value in deck:
            encrypted_deck.append(alice_key.card_encrypt(str(value)))
        
        print("Encrypted Deck is: ", encrypted_deck)
        cardDeck.setDeck(encrypted_deck)

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                             Shuffling Deck + Sending Deck to Bob                         ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        cardDeck.shuffle()
        print("Shuffled deck is: ", cardDeck.getDeck())

        s.connect((HOST, PORT))
        print()
        s.sendall(str(cardDeck.getDeck()).encode())

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                      Receiving Own Cards                                 ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        data = s.recv(4096)
        data_bob = Data.decode(data)
        print("Received: ", data_bob)

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                Decrypting Cards to Get Own Hand                          ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        aliceCards = []
        for value in data_bob:
            aliceCards.append(alice_key.card_decrypt(value))

        aliceHand = Hand.Hand(aliceCards)
        print("Alice's's hand is : ", aliceHand.getHand())

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                 Receiving Bob's Encrypted Cards                          ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        data = s.recv(4096)
        data_bob = Data.decode(data)
        print("Received: ", data_bob)

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                      Decrypting Bob's Cards                              ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        bobCardsB = []
        for value in data_bob:
            bobCardsB.append(alice_key.alice_decrypt_bob(value))
        print("Bob's decrypted cards: ", bobCardsB)
        s.sendall(str(bobCardsB).encode())

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                Receiving Bob's Key + Sending Own                         ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        data = s.recv(4096)
        print("Received: ", data)
        bob_key = key.key(int(data))
        bobCards = []
        for value in bobCardsB:
            bobCards.append(bob_key.card_decrypt(value))

        bobHand = Hand.Hand(bobCards)
        print("Bob's's hand is : ", bobHand.getHand())

        e_alice, d_alice = alice_key.return_keys()
        s.sendall(str(d_alice).encode())

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                      Results of the Game                                 ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        winner = Winner.Winner(aliceCards,bobCards).getWinner()
        if (winner == 1):
            print("Alice wins !!")
        else:
            print("Bob wins!!")

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                      Check Cheating                                      ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        e_key, d_key = alice_key.return_keys()
        s.sendall(str(e_key).encode())
        bob_e_key = s.recv(1024)
        print("Bob's Encryption Key is : ", bob_e_key.decode())
        s.sendall(str(d_key).encode())
        bob_d_key = s.recv(1024)
        print("Bob's Decryption Key is : ", bob_d_key.decode())

        results = []
        for value in bobCardsB:
            results.append(alice_key.decrypt_other(value, bob_d_key.decode()))
        print(results) #returning bob's hand in terms of numbers 
        BobsHand = Hand.Hand(results)
        print(BobsHand.getHand())

        #Now I check if what i receive from bob is the same as what bob sent earlier 
        if (BobsHand.getHand()==bobHand.getHand()):
            print("There has been no cheating!")
        else:
            print("There has been cheating!!!!")


        break

        #print("Encrypted Bob Message using Alice Key: ", alice_encrypt_bob(data_bob))

        
        #print("Encrypted Bob message with Alice Key: ", long_to_bytes(alice_encrypt(data_bob)))
        







    
    