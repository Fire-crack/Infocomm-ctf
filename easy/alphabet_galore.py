# flag = something

ciphertext = ""
alphabet = " abcdefghijklmnopqrstuvwxyz"

for i in flag:
    if i.isalpha():
        index = alphabet.find(i.lower())
        ciphertext += str(alphabet[-index])
    else:
        ciphertext += i

# ciphertext = xgurmulxlnn{ivevihvovggvih}
