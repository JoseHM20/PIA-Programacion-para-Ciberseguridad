# 🟣 PIA Cybersecurity 🟣

Cybersecurity tool 👮. Semester August-December 2021 👨‍🎓

![](https://seguridadinredeshome.files.wordpress.com/2019/08/bigstock-press-enter-button-on-the-keyb-220634140-1.jpg?w=900)

### INDEX  
1. [WARNING](#⚠-WARNING-⚠).
2. [Information about the authors](#Information-about-the-authors).
3. [Requirements](#Requirements).
4. [Repository installation](#Repository-installation).
5. [Project functionalities](#Project-functionalities).
6. [Project tools](#Project-tools).
7. [Modules used in the tool](#Modules-used-in-the-tool).
8. [Steps for execution](#Steps-for-execution).
9. [How to use the tool](#How-to-use-the-tool).
11. [Links for interested persons](#Links-for-interested-persons).  
  
### ⚠ WARNING ⚠
**🕵 This repository was created for educational purposes and at no time is expected to be used for actions that may affect other third parties 🕵**  
  
### Information about the authors
**Authors:**  
🟡 [Jose Luis Hernandez Meza](https://github.com/JoseHM20)      
🟡 [Gerardo Gamez Serna](https://github.com/Gerardo0202)  
  
Project created in Mexico 🤓  
Created by Universidad Autonoma de Nuevo Leon students 🏣  
Students from the School of Ciencias Fisico Matematicas 👨‍🏫  
  
![](https://www.uanl.mx/wp-content/uploads/2018/10/85-aniversario-uanl-torre-rectoria.jpg)  
  
### Project functionalities  
- Obtaining metadata from images coming directly from the camera.  
- Encrypt, decrypt and crack messages with the help of the Caesar tool.  
- Login to Google.  
- Sending mails with Google (without verification).  
- Sending text messages  
- View system information  
- View geolocation and network information  
- Search public information of organizations  
  
### Requirements
- Have Python 3 installed 🖥
- Check the installation of all modules ✅
- Download all scripts and modules ⬇
- Maintain the license in the project 📜  
  
### Repository installation
**El repositorio lo puedes instalar desde tu linea de comandos usando el siguiente comando:**  
`gh repo clone JoseHM20/PIA-Cybersecurity`
  
### Project tools
🟦 Sending e-mails and text messages  
🟦 Encryption, decryption and cracking of messages  
🟦 Image metadata acquisition  
🟦 System and network information  
🟦 Obtaining information from organizations  
🟦 Capture keystrokes using KeyLogger  
  
### Modules used in the tool
🔴 Time  
🔴 Argparse  
🔴 Logging  
🔴 OS  
🔴 PyHunter  
🔴 Subprocess  
🔴 PIL  
🔴 PIL.ExifTags  
🔴 Twilio  
🔴 Configparser  
🔴 Smtplib  
🔴 MIMEText  
🔴 MIMEMultipart  
🔴 MIMEBase  
  
### Steps for execution
1. Start the command prompt  
2. We go to the folder in which we saved the project  
3. Install the necessary modules using the file "requirements.txt"  
`pip install -r requirements.txt`  
5. You must make use of the main file, which will give the proper functioning of the tool  
![](https://github.com/JoseHM20/PIA-Cybersecurity/blob/f56e145e04df063840e83a053693f7b90aa7fa36/images/main.jpg)   
4. Execute the script with the "-h" to see the arguments
![](https://github.com/JoseHM20/PIA-Cybersecurity/blob/91c07773aac6f987bdd62f829c91cc90a49a4e32/images/argumentos%20CMD.jpg) 
  
### How to use the tool
**☑ Sending e-mails and text messages**  
Arguments to use in this tool  
SMS 📱
- "-org"
- "-dest"
- ".sms"  
![](https://github.com/JoseHM20/PIA-Cybersecurity/blob/main/images/msm.png)
E-mail ✉
- "-sendM"
- "-recivM"
- "-passw"
- "-sub"
- "-file"
- "-body"  
![](https://github.com/JoseHM20/PIA-Cybersecurity/blob/main/images/smail.png)
**☑ Encryption, decryption and cracking of messages**  
Arguments to use in this tool  
- "-mode"
- "-message"
- "-key"  
![](https://github.com/JoseHM20/PIA-Cybersecurity/blob/main/images/ccesar.png)
**☑ Metadata of Img to analyze**  
Arguments to use in this tool  
- "-ruta"  
  
**☑ System and network information**  
Arguments to use in this tool  
Bash 🐧  
🟢 This tool should preferably be used in a Linux environment 🟢  
The tool is automated 🤖  
  
PowerShell ⌨  
🟢 This tool will only ask for the name of a service and the action you want to do with it 🟢  
  
**☑ Obtaining information from organizations**  
🟢 This tool will only ask for the domain of the organization to be investigated 🟢  
  
**❗ IMPORTANT NOTES ❗**  
  
🟡 In the SMS sending tool you will have to modify the configuration file with the values given by the Twilio platform.  
🟡 It is essential to use "-tool" to specify with a number from 1 to 4 the tool to use.  
🟡 The tool for obtaining information from organizations is independent from the main file, so you must run it separately.  
🟡 The Keylogger application is a basic example and is also independent of the main file.  
  
### Links for interested persons
- [Python Installation](https://www.python.org/)
- [Create your company for automated messages and calls](https://www.twilio.com/)
- [Learn how to use Twilio](https://www.twilio.com/blog/enviar-mensaje-whatsapp-30-segundos-con-python)
- [Send emails with SMTP](https://code.tutsplus.com/es/tutorials/sending-emails-in-python-with-smtp--cms-29975)
- [Learn how to use Caesar in your messages](https://www.instintoprogramador.com.mx/2020/11/cifrado-caesar-en-python-tutorial-de.html)
- [Get the information from your photos](https://es.acervolima.com/2021/02/09/como-extraer-metadatos-de-imagenes-en-python/)
