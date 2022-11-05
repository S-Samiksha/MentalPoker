# Adapted from https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/ 


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

import Global
import socket
import pickle, json


parameters = Global.return_paramter()

# Generate a private key for use in the exchange.
Alice_private_key = parameters.generate_private_key()
#Generate the public key associated with the private key 
Alice_public = Alice_private_key.public_key()
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 53142  # The port used by the server




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = vars(Alice_public)
    msg = pickle.dumps(data)
    Bob_public = s.recv(4096)
    print(f"Received {Bob_public!r}")


shared_key = Alice_private_key.exchange(pickle.loads(Bob_public))

