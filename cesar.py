# Cifra de Cesar

alfabeto = 'abcdefghijklmnopqrstuvwyz éá'
max_alf = len(alfabeto)

def cesar(texto, rotacao=13):
    resultado = []
    for char in texto:
        pos = alfabeto.find(char)
        if pos == -1:
            resultado.append(char)
            continue
        pos = pos + rotacao
        while(pos >= max_alf):
            pos = pos - max_alf
        resultado.append(alfabeto[pos])
        
    return "".join(resultado)
    
def reverte_cesar(texto, rotacao=13):
    resultado = []
    for char in texto:
        pos = alfabeto.find(char)
        if pos == -1:
            resultado.append(char)
            continue
        pos = pos - rotacao
        while(pos < 0):
            pos = pos + max_alf
        resultado.append(alfabeto[pos])
        
    return "".join(resultado)

texto = "Olá meu nome é Felipe"
print(texto)
c = cesar(texto)
print(c)
o = reverte_cesar(c)
print(o)