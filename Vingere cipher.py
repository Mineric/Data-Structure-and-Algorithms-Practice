#Vingere Cipher
cipher = input("Ciphertext: ")
key = str(input("Decryption key: "))
k = []
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in key:
    k.append(alphabet.find(i))

Plaintext=''
for i in cipher:
    for j in k:
        print(type(key))
        Plaintext += alphabet[(j-key)%52]

print("Plaintext: ", Plaintext)
