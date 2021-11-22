# flag = something
ciphertext = ""

for i in range(0, 30, 10):
    for j in range(10, -1, -1):
        # print(i)
        ciphertext += flag[i+j]


print(ciphertext)

# ciphertext = mmocofnIFTCera_sp00l{m}!gnizama_e
