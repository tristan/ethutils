from secp256k1 import PrivateKey
from ethutils.data import data_decoder, data_encoder
from ethutils.hashing import sha3

def private_key_to_address(private_key):
    """Extracts the address from the given private key, returning the
    hex representation of the address"""

    if isinstance(private_key, str):
        private_key = data_decoder(private_key)

    return data_encoder(sha3(PrivateKey(private_key).pubkey.serialize(False)[1:])[12:])
