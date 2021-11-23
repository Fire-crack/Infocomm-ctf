# flag = something

import string, random

ciphertext = ""
for i in flag:
    ciphertext += str(i + random.choice(string.ascii_letters))

    
# output = CWThFbIpnQfEoVcxommymZ{OqLwLexrjtOyd}g
