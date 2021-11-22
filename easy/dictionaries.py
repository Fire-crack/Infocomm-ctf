# flag = something

def convert(letter):
    lowered = letter.lower()

    mapping = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        '{': '`',
        '}': '=',
        '_': '-',
        '0': ')',
        '1': '!',
        '2': '@',
        '3': '#',
        '4': '$',
        '5': '%',
        '6': '^',
        '7': '&',
        '8': '*',
        '9': '(',
        '!': '+'
    }

    return str(mapping[lowered])

ciphertext = ""

for char in flag:
    ciphertext += convert(char) + ' '


print(ciphertext)
# ciphertext = 3 20 6 9 14 6 15 3 15 13 13 ` + 4 9 3 20 19 - 1 18 # - 6 21 14 =
