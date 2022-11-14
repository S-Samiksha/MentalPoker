# Adapted from https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/ 

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import Global
import socket
import pickle


parameters = Global.return_paramter()

# Generate a private key for use in the exchange.
Bob_private_key = parameters.generate_private_key()
#Generate the public key associated with the private key 
Bob_public = Bob_private_key.public_key()

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 53142  # Port to listen on (non-privileged ports are > 1023)


while (True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                Alice_public = conn.recv(4096)
                if not Alice_public:
                    break

                print(Alice_public)
                if Alice_public.decode() == "end":
                    s.close() 
                    exit()
                msg = pickle.dumps(Bob_public)
                conn.sendall(msg)

shared_key = Bob_private_key.exchange(pickle.loads(Alice_public))


