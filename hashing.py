import hashlib

def hash_key(key):
    hashing_func = hashlib.sha512()

    hashing_func.update(bytes(key, "ASCII"))

    return hashing_func.digest()
