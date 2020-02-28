import hashlib

def hash_key(key, repetitions=4):
    def perform_hash(key):
        hashing_func = hashlib.sha512()

        hashing_func.update(key)

        return hashing_func.digest()

    def iterate(key, repetitions):
        if repetitions == 0:
            return perform_hash(key)

        center = len(key)//2

        left_side = key[:center]
        right_side = key[center:]

        return iterate(left_side, repetitions-1) + iterate(right_side, repetitions-1)
        

    res = perform_hash(bytes(key, "ASCII"))
        

    return iterate(res, repetitions)
