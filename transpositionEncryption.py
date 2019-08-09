# http://inventwithpython.com/hacking (BSD Licensed)
import pyperclip

def main():
    myMessage = input('Please type the message to be encrypted: ') 
    myKey = int(input('Please input your key(int): '))

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
        
    #Creates an empty string and adds ciphertext as a single string
    return ''.join(ciphertext)

if __name__ == "__main__":
    main()