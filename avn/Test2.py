from cryptography.fernet import Fernet
import base64
# 
txt = "segredoAqui_esta_sendo_salvoAqui" #32 chars
print(txt)
txt = txt.encode('ascii')
print(txt)
key = base64.b64encode(txt)
print(key)

f = Fernet(key)
token = f.encrypt(b"Mensagem secreta.")
print(token)

t = f.decrypt(token)
print(t)
