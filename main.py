# PIA - Producto Integrador de Aprendizaje
# Universidad Autonoma de Nuevo Leon
# Facultad de Ciencias Fisico Matematicas

# Participantes:
# Jose Luis Hernandez Meza
# Gerardo Gamez Serna 
# Francisco Javier Valerio Lara

# Import of modules
import time
import argparse
import logging
import SendSE
import CIFCesar
import MetaIMG
import Internal


def main():
    # Main application menu
    if work == "1":
        # Email and text message sending tool
        print("\nYou have selected option 1")
        print("Starting tool...\n")
        time.sleep(2)
        logging.info('Se ha iniciado la herramienta No.1')
        SendSE.Contact(DESTINATION, ORIGIN, SMS, sendMail, reciveMail, password, subject, text, filename)
    elif work == "2":
        # Tool for encrypting, decrypting and cracking messages
        print("\nYou have selected option 2")
        print("Starting tool...\n")
        time.sleep(2)
        logging.info('Se ha iniciado la herramienta No.2')
        CIFCesar.Cesar(mod, message, key)
    elif work == "3":
        # Tool to analyze image information
        print("\nYou have selected option 3")
        print("Starting tool...\n")
        time.sleep(2)
        logging.info('Se ha iniciado la herramienta No.3')
        MetaIMG.printMeta(ruta)
    elif work == "4":
        # Use of tools in other programming languages
        print("\nYou have selected option 4")
        print("Starting tool...\n")
        time.sleep(2)
        logging.info('Se ha iniciado la herramienta No.4')
        Internal.ScriptPB()
    else:
        print("\nYou did not select any option")


if __name__ == "__main__":
    # Start argparse
    parser = argparse.ArgumentParser(
        description="Cybersecurity tool"
    )

    # We add the required arguments

    # Choice of tool to use
    parser.add_argument(
        "-tool",
        type=str,
        help="Type the tool you want to use (1-5)")
    # Arguments for sending text messages
    parser.add_argument(
        "-org",
        type=str,
        help="Enter your Twilio number")
    parser.add_argument(
        "-dest",
        type=str,
        help="Enter the destination number")
    parser.add_argument(
        "-sms",
        nargs="?",
        default="This message comes from the PC PIA",
        type=str,
        help="Add the message to be sent via SMS")

    # Arguments for sending e-mails
    parser.add_argument(
        "-sendM",
        type=str,
        help="Type the email address from which the email will be sent ")
    parser.add_argument(
        "-recivM",
        type=str,
        help="Enter the email address of the recipient of the email")
    parser.add_argument(
        "-passw",
        type=str,
        help="Enter your email password")
    parser.add_argument(
        "-sub",
        type=str,
        help="Type the subject of your email")
    parser.add_argument(
        "-file",
        type=str,
        help="Type the name of your file")
    parser.add_argument(
        "-body",
        type=str,
        help="Write the body of your email")

    # Arguments for the Caesar tool
    parser.add_argument(
        "-mode",
        nargs="?",
        default="e",
        type=str,
        help="Type the working mode: 'e' for encrypt, 'd' for decrypt or 'c' for crack message.")
    parser.add_argument(
        "-message",
        nargs="?",
        default="Soy LSTI y me gusta programar",
        type=str,
        help="Type the message to use")
    parser.add_argument(
        "-key",
        nargs="?",
        default="clave del dia",
        type=str,
        help="Type the message to use")

    # Argument of the image to analyze with the metadata tool
    parser.add_argument(
        "-ruta",
        type=str,
        help="Type the location of your image")

    args = parser.parse_args()

    # We redefine the arguments
    # This will make it easier to use during development
    work = args.tool
    ORIGIN = args.org
    DESTINATION = args.dest
    SMS = args.sms
    sendMail = args.sendM
    reciveMail = args.recivM
    password = args.passw
    subject = args.sub
    text = args.body
    filename = args.file
    mod = args.mode
    message = args.message
    key = len(args.key)
    ruta = args.ruta

    print("========================================")
    print("-----------INICIANDO PROGRAMA-----------")
    print("========================================")

    time.sleep(2)

    print("Programacion para Ciberseguridad")

    time.sleep(1)

    main()
