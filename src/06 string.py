import pdb
MAX_ASCII = 256


def de_dup(word: str):
    result = []
    h = [0] * MAX_ASCII
    for char in word:
        if h[ord(char)] == 0:
            result.append(char)
            h[ord(char)] = 1
    return ''.join(result)


print(de_dup('Data'))
