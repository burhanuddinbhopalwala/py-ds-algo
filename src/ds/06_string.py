from stack import reverse_string_stack

MAX_ASCII = 256


def maxm_occurence(word: str):
    h = [0] * MAX_ASCII
    for char in word:
        h[ord(char)] += 1

    return chr(h.index(max(h)))
################################################################################

# print(maxm_occurence("Burhanuddin"))


def de_dup(word: str):
    result = []
    h = [0] * MAX_ASCII
    for char in word:
        if h[ord(char)] == 0:
            result.append(char)
            h[ord(char)] = 1
    return ''.join(result)


# print(de_dup('Data'))
################################################################################

def check_rotation(word1, word2):
    # return sorted(word1) == sorted(word2)
    concat = word1 + word1
    return concat.find(word2)  # * 1, -1


# print(check_rotation("madam", "adamm"))
################################################################################

def is_palindrome(word):
    return word == reverse_string_stack(word)


# print(is_palindrome("madam"))
################################################################################

def first_non_repeating_char(word: str):
    store = {}
    for index, char in enumerate(word):
        if char in store:
            store[char][1] += 1
        else:
            store[char] = [index, 1]

    first_minm = -1 * len(word)
    for key, value in store.items():
        if first_minm > int(value[0]) and int(value[1]) == 1:
            first_minm = key
    return word[first_minm]


print(first_non_repeating_char('Burhanuddin'))
################################################################################

# * Pending: Maxm and Minm with minm no of comparisons
