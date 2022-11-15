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
from Alice_func import *
import Deck
import Hand

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~ Alice ready to play ~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 53140  # The port used by the server

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        print()
        print("~~~~~~~~~~~~~~~~~~~~~ Alice Creating Deck ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        cardDeck = Deck.Deck()
        deck = cardDeck.getDeck() #deck is a list 
        print("Deck is: ", deck)


        print("~~~~~~~~~~~~~~~~~~~~~ Alice Encrypting Deck ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        encrypted_deck = []
        for value in deck:
            encrypted_deck.append(alice_encrypt(str(value)))
        
        print("Encrypted Deck is: ", encrypted_deck)
        cardDeck.setDeck(encrypted_deck)

        print("~~~~~~~~~~~~~~~~~~~~~ Alice Shuffling Deck ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        cardDeck.shuffle()
        print("Shuffled deck is: ", cardDeck.getDeck())


        print("~~~~~~~~~~~~~~~~~~~~~ Alice Sending Deck ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s.connect((HOST, PORT))
        s.sendall(str(cardDeck.getDeck()).encode())

        print("~~~~~~~~~~~~~~~~~~~~~~ Alice Waiting ~~~~~~~~~~~~~~~~~~~~~~~~~")
        data = s.recv(4096)
        data_bob = data.decode()
        print("Received from Bob: ", data_bob)

        print("~~~~~~~~~~~~Alice decrypts her own cards~~~~~~~~~~")
        temp1 = data_bob.replace("'", "")
        temp = temp1.strip('][').split(', ')
        print(temp)
        results = []
        for value in temp:
            results.append(alice_decrypt(value))

        aliceHand = Hand.Hand(results)
        print("Alice's hand is : ", results)
        print(aliceHand.getHand())


        print("~~~~~~~~~~~~~~~~~ Alice Waiting ~~~~~~~~~~~~~~~~~")
        data_B = s.recv(4096)
        data_BoB = data_B.decode()

        temp1 = data_BoB.replace("'","")
        temp = temp1.strip('][').split(',')
        print(temp)
        results = []
        for value in temp:
            results.append(alice_decrypt_bob(value))
        

        print("Bob's encrypted hand is: ", results)
        s.sendall(str(results).encode())
       
        break

        #print("Encrypted Bob Message using Alice Key: ", alice_encrypt_bob(data_bob))

        
        #print("Encrypted Bob message with Alice Key: ", long_to_bytes(alice_encrypt(data_bob)))
        







    
    