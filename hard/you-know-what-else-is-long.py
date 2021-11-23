# yeah you're gonne be dealing with long numbers

# flag is in the form of CTFInfocomm{num}

num = int(flag[12:-1])


def to_b27(num):
    """Converts to base 27
    Example:
    >>> to_b27(26)
    'z'
    >>> to_b27(27)
    'aa'
    >>> to_b27(53)
    'ba'
    """

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    ret = ""
    while num != 0:
        num, rem = divmod(num - 1, 26)
        ret += alphabets[rem]

    return ret[::-1]


ciphertext = to_b27(num)
# ciphertext = bkmygeoiowwmqwnwkyvuxzyghjbbzzloxeu
