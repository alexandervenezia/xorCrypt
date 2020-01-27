import os

#Encrypts the contents of a file, or, if it has already been encrypted, decrypts it.
def encryptDecrypt(initial, key):
    final = bytearray()
    keyIndex = 0
    for byte in initial:
        final.append(byte^key[keyIndex])
        keyIndex += 1
        if keyIndex >= len(key):
            keyIndex = 0

    return final

#Finds all files in a directory structure
def getFiles(folder):
    files = []
    for file in os.listdir(folder):
        if os.path.isfile(folder+"/"+file):
            files.append(folder+"/"+file)
        elif os.path.isdir(folder+"/"+file):
            for f in getFiles(folder+"/"+file):
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

rawKey = key
key = bytearray(key, "ascii")

#If the user entered the path to a file, perform the encryption operation on that file
if os.path.isfile(path):
    file = open(path, "rb")
    data = file.read()
    file.close()


    if input("Your key is: " + rawKey + ". Continue? (y/n) ") == 'y': #Verify that the user wants to proceed
        file = open(path, "wb")
        file.write(encryptDecrypt(data, key))
        file.close()

#If the user entered the path to a directory, find all subfiles and apply the encryption operation
elif os.path.isdir(path):
    if input("Your key is: " + rawKey + ". Continue? (y/n) ") == 'y': #Verify that the user wants to proceed
        for filename in getFiles(path):
            file = open(filename, "rb")
            data = file.read()
            file.close()

            file = open(filename, "wb")
            file.write(encryptDecrypt(data, key))
            file.close()
