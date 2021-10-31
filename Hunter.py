from pyhunter import PyHunter
from openpyxl import Workbook
import time

h = PyHunter("")

def busqueda(organi):
    # Information search function
    busq = 1
    r = h.domain_search(company=organi, limit=busq, emails_type='personal')
    return r

def guardarInformacion(datosEncontrados, organizacion):
    # Function to save the information obtained
    try:
        file = open("Hunter.txt", "w") # Create file to save the information
    except OSError:
        print("No se ha podido abrir el archivo")

    file.write("Domain information\n")
    file.write(str(datosEncontrados)) # We use the information found
    file.close()

def HUNTER():
    print("======================")
    print("Search for information")
    print("======================")

    time.sleep(2)
    
    try:
        orga = input("Write your domain: ")
        datosEncontrados = busqueda(orga)
        if datosEncontrados == None:
            exit()
        else:
            print(datosEncontrados)
            print(type(datosEncontrados))
            guardarInformacion(datosEncontrados, orga)
    except KeyboardInterrupt:
        print("Se ha interrumpido el script")
        
HUNTER()
