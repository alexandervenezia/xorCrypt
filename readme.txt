A simple xor cipher, which can be applied to files of any type. Running the program on an encrypted file will undo the encryption as long as the same key is provided.

The xor cipher is a type of additive cipher. Each byte of the plaintext is xored with the corresponding byte of the key. The key will be repeated as many times as necessary to fully encrypt the plaintext.

The strength of the xor cipher is directly proportional to the length and randomness of key used. Theoretically, if the key was truly random and of equal or greater length as the plaintext, it would constitute a one time pad and be unbreakable. However, as keys of such length are unwieldy, in practice the basic xor cipher is unsuitable for any task requiring serious security.