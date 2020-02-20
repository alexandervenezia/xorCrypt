import os, hashing

#Encrypts the contents of a file, or, if it has already been encrypted, decrypts it.
def encrypt_decrypt(initial, key):
    final = bytearray()
    keyIndex = 0
    for byte in initial:
        final.append(byte^key[keyIndex])
        keyIndex += 1
        if keyIndex >= len(key):
            keyIndex = 0

    return final

#Finds all files in a directory structure
def get_files(folder):
    files = []
    for file in os.listdir(folder):
        if os.path.isfile(folder+"/"+file):
            files.append(folder+"/"+file)
        elif os.path.isdir(folder+"/"+file):
            for f in get_files(folder+"/"+file):
                files.append(f)

    return files

path = input("File or directory to encrypt/decrypt: ")

while not os.path.exists(path):
    print("Invalid path.")
    path = input("File or directory to encrypt/decrypt: ")

verified = False

while not verified:
    key = input("Key: ")
    if input("Verify key: ") != key:
        print("Keys do not match, try again.")
    else:
        verified = True

raw_key = key
#key = bytearray(key, "ascii")
key = hashing.hash_key(key)

#If the user entered the path to a file, perform the encryption operation on that file
if os.path.isfile(path):
    file = open(path, "rb")
    data = file.read()
    file.close()


    if input("Your key is: " + raw_key + ". Continue? (y/n) ") == 'y': #Verify that the user wants to proceed
        file = open(path, "wb")
        file.write(encrypt_decrypt(data, key))
        file.close()

#If the user entered the path to a directory, find all subfiles and apply the encryption operation
elif os.path.isdir(path):
    if input("Your key is: " + raw_key + ". Continue? (y/n) ") == 'y': #Verify that the user wants to proceed
        for filename in get_files(path):
            file = open(filename, "rb")
            data = file.read()
            file.close()

            file = open(filename, "wb")
            file.write(encrypt_decrypt(data, key))
            file.close()
