# http://inventwithpython.com/hacking (BSD Licensed)
import pyperclip

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = input("Please type in the message to be translated: ")
message = message.upper()

mode = input("Please select 'encrypt' or 'decrypt':")

key = int(input("Please type in the encryption key (0 - 25): "))

translated = ""

for letter in message:
    if letter in ALPHABET:
        num = ALPHABET.find(letter)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        
        if num >= len(ALPHABET):
            num = num - len(ALPHABET)
        elif num < 0:
            num = num + len(ALPHABET)
        
        translated = translated + ALPHABET[num]

    else:
        translated = translated + letter

print(translated)
pyperclip.copy(translated)