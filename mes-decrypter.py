from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

priv_key =  '''-----BEGIN RSA PRIVATE KEY-----
                 Your RSA private key here
               -----END RSA PRIVATE KEY-----''' 

priv_key = RSA.import_key(priv_key)

cipher_rsa = PKCS1_OAEP.new(priv_key)

text = input("TESTO:")

text = bytes.fromhex(text)

dec_text = cipher_rsa.decrypt(text)

print(dec_text)