from cryptography.fernet import Fernet
import base64
# https://github.com/fernet/spec/blob/master/Spec.md
key = Fernet.generate_key()
print(key)
original_key = base64.b64decode(key + b'=')
print(original_key)

f = Fernet(key)
token = f.encrypt(b"Mensagem secreta.")
print(token)

t = f.decrypt(token)
print(t)
