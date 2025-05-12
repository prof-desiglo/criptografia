def c_exclusivo(texto, chave):
    resultado = []
    v = 0
    for t in texto:
        r = ord(t) ^ ord(chave[v])
        v = v + 1
        if v >= len(chave):
            v = 0
        resultado.append(chr(r))
    return "".join(resultado)

#####
res = ''.join(format(ord(i), '08b') for i in "O")
print(res)
#
res = ''.join(format(ord(i), '08b') for i in "s")
print(res)
#
v = chr(ord("O") ^ ord("s"))
res = ''.join(format(ord(i), '08b') for i in v)
print(res)
#
v = chr(ord(v) ^ ord("s"))
res = ''.join(format(ord(i), '08b') for i in v)
print(res)

################
cif = "segredo"
texto = "Olá meu nome é Felipe"
print(texto)
print(texto)
c = c_exclusivo(texto, cif)
print(c)
o = c_exclusivo(c, cif)
print(o)