import time
import os

dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
def Cesar(mod, message, key):

    print("============================================")
    print("Encrypting, decrypting and cracking messages")
    print("============================================")

    print("\n")
    time.sleep(2)

    if mod == "e":
        print("You have selected the message encryption option")
        message = message.upper()
        print("Your encrypted message is:")
        Fraenc = Encrypt(message, key) # Print encrypted message
    elif mod == "d":
        print("You have selected the message decryption option.")
        message = message.upper()
        print("our decrypted message is:")
        Frades = Decrypt(message, key) # Prints the decrypted message
    elif mod == "c":
        print("You have selected the message cracking option")
        message = message.upper()
        print("The cracked message is:")
        Fracrack = Crack(message, key) # Print cracked message

# Create the function that encrypts all messages
def Encrypt(message, key):
    translated = '' # We have an empty dictionary
    for symbol in message:
        if symbol in dict:
          try:
             symbolIndex = dict.find(symbol)
          except TypeError:
              print ("You have entered an invalid symbol")
          else:
            translatedIndex = symbolIndex + key
            if translatedIndex >= len(dict):
                   translatedIndex = translatedIndex - len(dict)
            elif translatedIndex < 0: #try:
                translatedIndex = translatedIndex + len(dict)
            
            translated = translated + dict[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)

# Create the function that will decrypt all messages
def Decrypt(message, key):
    translated = '' # We have an empty dictionary
    for symbol in message:
        if symbol in dict:
            try:
                symbolIndex = dict.find(symbol)
            except TypeError:
                print ("You have entered an invalid symbol")
            else:
               translatedIndex = symbolIndex - key
            if translatedIndex >= len(dict):
                translatedIndex = translatedIndex - len(dict)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(dict)
            translated = translated + dict[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)

# We create the function that will crack all messages using brute force
def Crack(message, key):
    for key in range(len(dict)):
        translated = '' # We have an empty dictionary
        for symbol in message:
            if symbol in dict:
                try:
                    symbolIndex = dict.find(symbol)
                except TypeError:
                    print ("You have entered an invalid symbol")
                else:
                    translatedIndex = symbolIndex - key
                if translatedIndex < 0: #try:
                    translatedIndex = translatedIndex + len(dict)
                translated = translated + dict[translatedIndex]
            else: #try:
                translated = translated + symbol
        print('Key #%s: %s' % (key, translated))
