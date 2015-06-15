#Jesse Bacon
#A couple of simple methods to encode a message using the Zen of Python module
from this import d as codex
def Zen_Python_decode(message):
    split_message = message.split(' ')
    dec_message = []
    for word in split_message:
        dec_word = ''
        for letter in word:
            if letter in codex.keys():
                dec_word += codex[letter]
            else:
                dec_word += letter
        dec_message.append(dec_word) 
    return(str.join(' ', dec_message))

def Zen_Python_encode(message):
    encoded_message = ''
    for letter in message:
        if letter in codex.keys():
            encoded_message += codex[letter]
        else:
            encoded_message += letter
    return encoded_message
m = Zen_Python_encode('The quick brown fox jumped over the lazy dog!')
Zen_Python_decode(m)