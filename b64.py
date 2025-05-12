import base64

txt = "Olá meu nome é Felipe"
b = base64.b64encode(txt.encode("utf-8"))
print(b)

ab = base64.b64decode(b)
print(ab.decode("utf-8"))