from pyhunter import PyHunter
from openpyxl import Workbook
import time

h = PyHunter('2c8c60c4db5b0e007336108085725c73aa44ec35')

def search(organi):
    # Information search function
    busq = 1
    r = h.domain_search(company=organi, limit=busq, emails_type='personal')
    return r

def SaveInfo(dataFound, organizacion):
    # Function to save the information obtained
    try:
        file = open("Hunter.txt", "w") # Create file to save the information
    except OSError:
        print("File could not be opened")

    file.write("Domain information\n")
    file.write(str(dataFound)) # We use the information found
    file.close()

def HUNTER():
    print("======================")
    print("Search for information")
    print("======================")

    time.sleep(2)
    
    try:
        orga = input("Write your domain: ")
        dataFound = search(orga)
        if dataFound == None:
            exit()
        else:
            print(dataFound)
            print(type(dataFound))
            SaveInfo(dataFound, orga)
    except KeyboardInterrupt:
        print("The script has been interrupted")

HUNTER()
