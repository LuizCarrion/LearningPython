ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Paste the encrypted message: ")

for key in range(len(ALPHABET)):
    translated = ""
    for letter in message:
        if letter in ALPHABET:
            num = ALPHABET.find(letter)
            num = num - key
        
            if num >= len(ALPHABET):
                num = num - len(ALPHABET)
            elif num < 0:
                num = num + len(ALPHABET)
        
            translated = translated + ALPHABET[num]

        else:
            translated = translated + letter
    
    print('Key #%s: %s' % (key,translated))
