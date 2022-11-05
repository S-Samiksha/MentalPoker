# Adapted from https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/ 


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


PARAMETER = dh.generate_parameters(generator=2, key_size=512)
results = PARAMETER.parameter_numbers()


def return_paramter():
    print(results.p, results.g)
    return PARAMETER