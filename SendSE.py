from twilio.rest import Client
import configparser
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time


# Sending e-mails and text messages

def Contact(DESTINATION, ORIGIN, SMS, sendMail, reciveMail, password, subject, text, filename):
    print("=============================================================")
    print("This tool will take care of sending e-mails and text messages")
    print("=============================================================")

    print("\n")
    time.sleep(2)

    op = input("\nType '1' to send a text message or '2' to send an e-mail: ")
    if op == "1":
        print("\nI select the text message sending option")
        SMSend(DESTINATION, ORIGIN, SMS)
    elif op == "2":
        print("\nI select the option to send e-mails")
        MAILsend(sendMail, reciveMail, password, subject, text, filename)
    else:
        print("\nYou did not select any option")
        print("Exiting...")
        time.sleep(2)
        exit()


def SMSend(DESTINATION, ORIGIN, SMS):
    config = configparser.ConfigParser()
    config.read("Twilio.cfg")

    SID = config["ACCESO"]["Account"]
    TOKEN = config["ACCESO"]["Auth"]

    customer = Client(SID, TOKEN)
    try:
      message = customer.messages.create(to=DESTINATION, from_=ORIGIN, body=SMS)
    except OSError:
        print("No se han encontrado los datos necesarios")
    else:
       print("The message has been sent")
       print("The message was received by the number:", message.to)
       print("It was sent from the number:", message.from_)
       print(message.body)


def MAILsend(sendMail, reciveMail, password, subject, text, filename):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sendMail
    message["To"] = reciveMail

    text = MIMEText(text, "plain")

    with open(filename, "rb") as attachment:
        # The content type "application/octet-stream" means that a MIME attachment is a binary file
        part2 = MIMEBase("application", "octet-stream")
        part2.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part2)

    # Add header
    part2.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(text)
    message.attach(part2)

    # Create secure connection with server and send email
    try:
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
          server.login(sendMail, password)
          server.sendmail(
              sendMail, reciveMail, message.as_string()
          )
    except OSError:
        print("No se ha podido mandar el correo")