cont = True
while cont:
    # Ask for encryption or decryption
    choice = input('(e)ncrypt or (d)ecrypt: ')
    while choice.lower() != 'e' and choice.lower() != 'd':
        print('Error!')
        choice = input('(e)ncrypt or (d)ecrypt: ')

    dictionary = {'a':'i', 'b':'d', 'c':'k', 'd':'s', 'e':'n', 'f':'l', 'g':'q', 'h':'v', 'i':'t', 'j':'m', 'k':'e', 'l':'b', 'm':'u', 'n':'g', 'o':'a', 'p':'x', 'q':'c', 'r':'z', 's':'f', 't':'w', 'u':'r', 'v':'y', 'w':'h', 'x':'o', 'y':'j', 'z':'p'}
    revDictionary = {value: key for key, value in dictionary.items()}
    if choice.lower() == 'd':
        # Ask for input
        str = input("Enter the encrypted message: ")
        str = str.lower()
        decryptedMsg = ""
        for x in str:
            if x in dictionary:
                decryptedMsg += dictionary[x]
            else:
                decryptedMsg += x
        print('\n\n')
        print('Decrypted Message: ' + decryptedMsg.upper())

    else:
        str = input("Enter message to encrypt: ")
        str.lower()
        encryptedMsg = ""
        for x in str.lower():
            if x in revDictionary:
                encryptedMsg += revDictionary[x]
            else:
                encryptedMsg += x
        print('\n\n')
        print('Encrypted Message: ' + encryptedMsg.upper())
    c = input('Would you like to continue? (y/n): ')
    while c.lower() != 'y' and c.lower() != 'n':
        print("Error!")
        c = input('Would you like to continue? (y/n): ')
    if c.lower() == 'n':
        cont = False
print('Goodbye')
