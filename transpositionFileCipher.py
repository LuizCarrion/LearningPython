# http://inventwithpython.com/hacking (BSD Licensed)
import transpositionEncryption, transpositionDecryption, time, os, sys

def main():
    inputFilename = input('Please type in the file name: ')
    outputFilename = 'outputFile.txt'
    myMode = input('Do you want to encrypt or decrypt this file? ')
    myKey = int(input('Please type in the key: '))

    #if the input file doest not exist, then the program terminates early
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting... ' % (inputFilename))
        sys.exit()
    
    #warns user that theres already a file with this name, givin an option to continue or quit.
    #the file WILL be overwritten in case the user select continue
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    
    #reads the file and stores its content
    fileObj= open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing... ' % (myMode.title()))

    #measure how long the encryption/decryption takes
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncryption.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecryption.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    #write the translated message to the output file
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__ == "__main__":
    main()

