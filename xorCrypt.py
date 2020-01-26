import os

def encryptDecrypt(initial, key):
    final = bytearray()
    keyIndex = 0
    for byte in initial:
        final.append(byte^key[keyIndex])
        keyIndex += 1
        if keyIndex >= len(key):
            keyIndex = 0

    return final

def getFiles(folder):
    files = []
    for file in os.listdir(folder):
        if os.path.isfile(folder+"/"+file):
            files.append(folder+"/"+file)
        elif os.path.isdir(folder+"/"+file):
            for f in getFiles(folder+"/"+file):
                files.append(f)

    return files

path = input("File to encrypt: ")

key = input("Key: ")
if input("Verify key: ") != key:
    raise Exception("Key mismatch")

rawKey = key
key = bytearray(key, "ascii")

if os.path.isfile(path):
    file = open(path, "rb")
    data = file.read()
    file.close()


    if input("Your key is: " + rawKey + ". Continue? (y/n) ") == 'y':
        file = open(path, "wb")
        file.write(encryptDecrypt(data, key))
        file.close()

elif os.path.isdir(path):
    if input("Your key is: " + rawKey + ". Continue? (y/n) ") == 'y':
        for filename in getFiles(path):
            file = open(filename, "rb")
            data = file.read()
            file.close()

            file = open(filename, "wb")
            file.write(encryptDecrypt(data, key))
            file.close()
