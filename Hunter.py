from pyhunter import PyHunter
from openpyxl import Workbook
import time

h = PyHunter('2c8c60c4db5b0e007336108085725c73aa44ec35')


def busqueda(organi):
    busq = 1
    r = h.domain_search(company=organi, limit=busq, emails_type='personal')
    return r


def guardarInformacion(datosEncontrados, organizacion):
    try:
        file = open("Hunter.txt", "w")
    except OSError:
        print("No se ha podido abrir el archivo")

    file.write("Domain information\n")
    file.write(str(datosEncontrados))
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
