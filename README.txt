========================================================================================================================================================================================================================================

This is an example of a basic ransomware program written in Python.

It is highly recommended to store the decryption tool in a secure location where it will not be affected by the ransomware. 
Not doing so may result in the permanent loss of access to your encrypted files.

The mes-decrypter.py is a file that can decrypt the password for the program you receive via email.

Before executing the program, you must modify the directory paths in the mrkrab.py file to initialize the ransomware correctly.

To create an executable from the provided mrkrab.py script, you can use the following pyinstaller commands, depending on your operating system:

Linux and Mac << pyinstaller --onefile --add-data "bg.png:." mrkrab.py --hidden-import='PIL._tkinter_finder' >>

Windows << pyinstaller --onefile --add-data "bg.png;." mrkrab.py --hidden-import='PIL._tkinter_finder' >>

** DISCLAIMER ** 

This software is intended for educational purposes only. Any unauthorized or illegal use of this software is strictly prohibited and will be the sole responsibility of the user.

** DISCLAIMER ** 

========================================================================================================================================================================================================================================