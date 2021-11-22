# flag = something

character_list = list(flag)
phrase = "".join(character_list[12:-1])

one, two, three, four, *the_rest = phrase
the_rest = the_rest[::-1]

ciphertext = "".join([two + three + one + four] + the_rest)


# ciphertext = 0ndtst51l_3v0l_3w_
