# Cifra de Cesar

def cesar(texto, rotacao=13):
    resultado = []
    for char in texto:
        v = ord(char) + rotacao
        resultado.append(chr(v))
    return "".join(resultado)
    
def reverte_cesar(texto, rotacao=13):
    resultado = []
    for char in texto:
        v = ord(char) - rotacao
        resultado.append(chr(v))
    return "".join(resultado)
    
def frequencia_letras(texto):
    freq = {}
    for t in texto:
        freq[t] = texto.count(t)
    return freq
    
    
texto = "Olá meu nome é Felipe"
print(texto)
c = cesar(texto)
print(c)
o = reverte_cesar(c)
print(o)

ff1 = frequencia_letras(texto)
ff2 = frequencia_letras(c)
print(ff1)
print(ff2)


texto = "Um Texto simples aqui usando a mesma cifra"
print(texto)
c = cesar(texto)
print(c)
print(c.encode('utf-8'))
o = reverte_cesar(c)
print(o)
ff1 = frequencia_letras(texto)
ff2 = frequencia_letras(c)
print(ff1)
print(ff2)

