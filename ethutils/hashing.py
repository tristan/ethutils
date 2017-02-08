from Crypto.Hash import keccak
sha3_256 = lambda x: keccak.new(digest_bits=256, data=x).digest()

def sha3(seed):
    if isinstance(seed, str):
        seed = seed.encode('utf-8')
    return sha3_256(seed)
