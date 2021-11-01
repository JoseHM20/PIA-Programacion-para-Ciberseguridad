import subprocess
import os
import time

def ScriptPB():
    print("=========================")
    print("Execution of environments")
    print("=========================")
    time.sleep(2)
    print("\n")
    print("Importing scripts...")
    print("\n")
    time.sleep(2)
    
    SS = input("Write [1] to view network information, or [2] to view system information: ")
    
    if SS == "1":
        try:
            codeSH = subprocess.call("./GeoIP.sh")
        except (OSError, NameError):
            print("Ejecute este codigo en Bash")
            exit()
        except KeyboardInterrupt:
            print("Ha interrumpido el script")
        else:
            print(codeSH)
            print("The script has been executed")
    elif SS == "2":
        try:
            psm = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy',
                            'Unrestricted',
                            './ServicePC.ps1'], cwd=os.getcwd())
        except (OSError, NameError):
            print("Vuelva a intentarlo en PS")
            exit()
        except KeyboardInterrupt:
            print("Ha interrumpido el script")
        else:
            result = psm.wait()
